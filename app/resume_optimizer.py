def build_analysis_messages(resume_text: str, jd_text: str) -> list[dict[str, str]]:
    system_prompt = (
        "你是资深招聘顾问与技术面试官。"
        "请严格基于用户提供的简历与JD做分析，避免编造经历。"
        "输出必须使用中文，并严格使用以下Markdown结构：\n"
        "## 匹配亮点\n"
        "- ...\n"
        "## 主要缺口\n"
        "- ...\n"
        "## 具体优化建议\n"
        "- ...\n"
        "建议务必可执行，聚焦可改写的简历内容。"
    )
    user_prompt = (
        f"【简历内容】\n{resume_text}\n\n"
        f"【目标岗位JD】\n{jd_text}\n\n"
        "请输出匹配分析。"
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def build_optimized_resume_messages(resume_text: str, jd_text: str, analysis_text: str) -> list[dict[str, str]]:
    system_prompt = (
        "你是专业简历优化顾问。"
        "请根据原简历和匹配分析，产出一版优化后的中文简历。"
        "要求：不伪造经历，不新增未提供事实；可重组结构、措辞量化、强调与JD匹配项。"
        "输出使用清晰Markdown结构，至少包含：个人概述、核心技能、项目经历、教育背景。"
    )
    user_prompt = (
        f"【原始简历】\n{resume_text}\n\n"
        f"【目标岗位JD】\n{jd_text}\n\n"
        f"【匹配分析】\n{analysis_text}\n\n"
        "请生成优化后的完整简历。"
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
