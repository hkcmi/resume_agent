from app.resume_optimizer import build_analysis_messages, build_optimized_resume_messages


def test_build_analysis_messages_shape() -> None:
    messages = build_analysis_messages("resume", "jd")
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert "匹配亮点" in messages[0]["content"]
    assert messages[1]["role"] == "user"


def test_build_optimized_resume_messages_shape() -> None:
    messages = build_optimized_resume_messages("resume", "jd", "analysis")
    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert "优化后的中文简历" in messages[0]["content"]
    assert messages[1]["role"] == "user"
