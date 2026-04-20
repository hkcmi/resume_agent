import argparse

from app.agent import ExamAgent
from app.llm_client import DeepSeekClient
from app.tools import normalize_prompt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple exam agent entrypoint")
    parser.add_argument("--prompt", required=True, help="User prompt")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompt = normalize_prompt(args.prompt)
    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    agent = ExamAgent(DeepSeekClient())
    result = agent.run(prompt)
    print(result)


if __name__ == "__main__":
    main()
