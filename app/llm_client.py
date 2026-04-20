from typing import Any

import requests

from app.config import Config


class DeepSeekAPIError(Exception):
    pass


class DeepSeekClient:
    def __init__(self) -> None:
        if not Config.deepseek_api_key:
            raise ValueError("DEEPSEEK_API_KEY is not set.")

    def chat(self, prompt: str) -> str:
        return self.chat_messages([{"role": "user", "content": prompt}])

    def chat_messages(self, messages: list[dict[str, str]], temperature: float = 0.2) -> str:
        url = f"{Config.deepseek_base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {Config.deepseek_api_key}",
            "Content-Type": "application/json",
        }
        payload: dict[str, Any] = {
            "model": Config.deepseek_model,
            "messages": messages,
            "temperature": temperature,
        }
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        if not response.ok:
            raise DeepSeekAPIError(f"DeepSeek API request failed: {response.status_code} {response.text}")
        data = response.json()
        return data["choices"][0]["message"]["content"]
