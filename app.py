import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_MODEL = "llama3.2:3b"
DEFAULT_BASE_URL = "http://localhost:11434"


def build_prompt(email_text: str, strategy: str = "zero-shot") -> str:
    if strategy == "zero-shot":
        return f"""You are an expert email assistant. Write a concise and professional reply to the email below.

Email:
{email_text}

Reply:
"""

    if strategy == "few-shot":
        return f"""You are an expert email assistant. Follow the style of the examples below and write a concise professional reply.

Example 1:
Email: Hi team, I am running late for the meeting today.
Reply: Hi team, thanks for letting me know. I will join as soon as possible and will share an update if there is any delay.

Example 2:
Email: Thanks for the update. Could you send the report by Friday?
Reply: Certainly, I will send the report by Friday. Please let me know if you need anything else.

Now reply to this email:
Email:
{email_text}

Reply:
"""

    if strategy == "chain-of-thought":
        return f"""You are an expert email assistant. First identify the intent of the email, then draft a short professional reply. Keep the reply polite, clear, and concise.

Email:
{email_text}

Plan:
1. Identify the main request or concern.
2. Write a polite and useful response.
3. Keep the tone professional.

Reply:
"""

    raise ValueError(f"Unsupported strategy: {strategy}")


def call_ollama(prompt: str, model: str = DEFAULT_MODEL, base_url: str = DEFAULT_BASE_URL) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.3},
    }
    request_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{base_url}/api/generate",
        data=request_data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            output = response.read().decode("utf-8")
            data = json.loads(output)
            return data.get("response", "").strip()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Ollama at {base_url}. Start Ollama and pull the model first. Error: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Unexpected response from Ollama: {exc}") from exc


def generate_reply(email_text: str, strategy: str = "zero-shot", model: str = DEFAULT_MODEL) -> str:
    prompt = build_prompt(email_text, strategy=strategy)
    return call_ollama(prompt, model=model)


def load_demo_dataset(path: str):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def run_demo(dataset_path: str, strategy: str, model: str) -> None:
    dataset = load_demo_dataset(dataset_path)
    for item in dataset[:3]:
        print(f"\nExample: {item['topic']}")
        print("Email:")
        print(item["email"])
        print("\nGenerated reply:")
        reply = generate_reply(item["email"], strategy=strategy, model=model)
        print(reply)
        print("-" * 60)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate email replies locally with Ollama")
    parser.add_argument("--email", help="Email content to reply to")
    parser.add_argument("--strategy", choices=["zero-shot", "few-shot", "chain-of-thought"], default="zero-shot")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--dataset", default=str(Path("data") / "synthetic_emails.json"))
    parser.add_argument("--demo", action="store_true", help="Run a quick demo with sample emails")
    args = parser.parse_args()

    if args.demo:
        run_demo(args.dataset, args.strategy, args.model)
        return

    if args.email:
        reply = generate_reply(args.email, strategy=args.strategy, model=args.model)
        print(reply)
        return

    print("No email provided. Use --email 'Your email here' or run --demo.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
