from app.tools import normalize_prompt
from app.tools import decode_uploaded_text, normalize_multiline_text, parse_analysis_sections


def test_normalize_prompt_trims_spaces() -> None:
    assert normalize_prompt("  hello  ") == "hello"


def test_normalize_multiline_text_trims_lines_and_edges() -> None:
    source = "  line1  \nline2   \n\n"
    assert normalize_multiline_text(source) == "line1\nline2"


def test_decode_uploaded_text_uses_utf8() -> None:
    assert decode_uploaded_text("简历".encode("utf-8")) == "简历"


def test_parse_analysis_sections_extracts_expected_blocks() -> None:
    text = (
        "## 匹配亮点\n"
        "- A\n"
        "## 主要缺口\n"
        "- B\n"
        "## 具体优化建议\n"
        "- C\n"
    )
    parsed = parse_analysis_sections(text)
    assert parsed["匹配亮点"] == "- A"
    assert parsed["主要缺口"] == "- B"
    assert parsed["具体优化建议"] == "- C"
