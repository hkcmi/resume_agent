from app.llm_client import DeepSeekClient


class ExamAgent:
    def __init__(self, llm_client: DeepSeekClient):
        self.llm_client = llm_client

    def run(self, prompt: str) -> str:
        return self.llm_client.chat(prompt)
