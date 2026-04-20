import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.llm_client import DeepSeekAPIError, DeepSeekClient
from app.resume_optimizer import build_analysis_messages, build_optimized_resume_messages
from app.tools import decode_uploaded_text, normalize_multiline_text, parse_analysis_sections


def _get_resume_text(uploaded_file, manual_resume: str) -> str:
    if uploaded_file is not None:
        return decode_uploaded_text(uploaded_file.getvalue())
    return normalize_multiline_text(manual_resume)


def main() -> None:
    st.set_page_config(page_title="简历优化 Agent", page_icon="🧠", layout="wide")
    st.title("🧠 简历优化 Agent")
    st.caption("输入/上传简历 + 输入目标JD，先分析匹配度，再确认生成优化版简历。")

    with st.sidebar:
        st.subheader("运行配置")
        st.write("请确保已通过环境变量设置 `DEEPSEEK_API_KEY`。")

    left, right = st.columns(2)

    with left:
        st.subheader("1) 输入简历")
        uploaded_file = st.file_uploader("上传简历文本文件（.txt/.md）", type=["txt", "md"])
        manual_resume = st.text_area("或直接粘贴简历内容", height=260, placeholder="请粘贴简历内容")

    with right:
        st.subheader("2) 输入目标JD")
        jd_text = st.text_area("粘贴职位描述（JD）", height=360, placeholder="请粘贴目标岗位JD")

    analyze_clicked = st.button("3) 分析简历与JD匹配情况", type="primary")
    if analyze_clicked:
        resume_text = _get_resume_text(uploaded_file, manual_resume)
        jd_text_clean = normalize_multiline_text(jd_text)
        if not resume_text:
            st.error("请先上传或输入简历内容。")
            return
        if not jd_text_clean:
            st.error("请先输入目标JD。")
            return
        try:
            client = DeepSeekClient()
            messages = build_analysis_messages(resume_text, jd_text_clean)
            analysis_text = client.chat_messages(messages)
        except (ValueError, DeepSeekAPIError) as exc:
            st.error(str(exc))
            return

        st.session_state["resume_text"] = resume_text
        st.session_state["jd_text"] = jd_text_clean
        st.session_state["analysis_text"] = analysis_text
        st.session_state["optimized_resume"] = ""

    if st.session_state.get("analysis_text"):
        st.subheader("4) 匹配分析结果")
        analysis_text = st.session_state["analysis_text"]
        sections = parse_analysis_sections(analysis_text)
        if any(sections.values()):
            for title, content in sections.items():
                st.markdown(f"### {title}")
                st.markdown(content if content else "- （模型未输出该部分）")
        else:
            st.markdown(analysis_text)

        confirmed = st.checkbox("我确认以上分析，并生成优化后的简历")
        if st.button("5) 生成优化后简历", disabled=not confirmed):
            try:
                client = DeepSeekClient()
                messages = build_optimized_resume_messages(
                    st.session_state["resume_text"],
                    st.session_state["jd_text"],
                    st.session_state["analysis_text"],
                )
                optimized_resume = client.chat_messages(messages, temperature=0.1)
            except (ValueError, DeepSeekAPIError) as exc:
                st.error(str(exc))
                return
            st.session_state["optimized_resume"] = optimized_resume

    if st.session_state.get("optimized_resume"):
        st.subheader("6) 优化后的简历")
        st.markdown(st.session_state["optimized_resume"])
        st.download_button(
            label="导出优化简历（.md）",
            data=st.session_state["optimized_resume"],
            file_name="optimized_resume.md",
            mime="text/markdown",
        )


if __name__ == "__main__":
    main()
