def normalize_prompt(text: str) -> str:
    return text.strip()


def normalize_multiline_text(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    normalized = "\n".join(lines).strip()
    return normalized


def decode_uploaded_text(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="ignore").strip()


def parse_analysis_sections(analysis_markdown: str) -> dict[str, str]:
    sections = {"匹配亮点": "", "主要缺口": "", "具体优化建议": ""}
    current = ""
    for raw_line in analysis_markdown.splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            title = line[3:].strip()
            if title in sections:
                current = title
                continue
        if current:
            sections[current] += (raw_line + "\n")
    return {key: value.strip() for key, value in sections.items()}
