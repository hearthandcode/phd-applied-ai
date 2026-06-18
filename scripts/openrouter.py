#!/usr/bin/env python3
"""
OpenRouter API Wrapper — Route prompts to any model via OpenRouter.
Captures token usage and logs cost. Designed for curriculum generation.

Usage:
  python3 openrouter.py --model anthropic/claude-sonnet-4 --prompt "What is..." [--system "You are..."] [--temp 0.7] [--max-tokens 4000] [--module M01] [--section "theory/02"]

  python3 openrouter.py --list-models              # List available models

  Or pipe a prompt:
  cat prompt.txt | python3 openrouter.py --model anthropic/claude-haiku-4

Environment:
  OPENROUTER_API_KEY  - Required. Your OpenRouter API key.
  OPENROUTER_BASE_URL - Optional. Default: https://openrouter.ai/api/v1

Output:
  JSON with: result, model, usage (prompt_tokens, completion_tokens),
             cost_usd, session_id
"""

import os, sys, json, argparse
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError

API_KEY = os.environ.get("OPENROUTER_API_KEY") or os.environ.get("HERMES_OPENROUTER_API_KEY")
BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# OpenRouter pricing per 1M tokens (approximate, as of 2026-06-18)
MODEL_PRICING = {
    "anthropic/claude-opus-4": {"input": 15.00, "output": 75.00},
    "anthropic/claude-sonnet-4": {"input": 3.00, "output": 15.00},
    "anthropic/claude-haiku-4": {"input": 0.25, "output": 1.25},
    "deepseek/deepseek-v4-flash": {"input": 0.15, "output": 0.60},
    "openai/gpt-4o": {"input": 2.50, "output": 10.00},
    "openai/o3-mini": {"input": 1.10, "output": 4.40},
    "google/gemini-2.0-flash-001": {"input": 0.10, "output": 0.40},
    "meta-llama/llama-3.3-70b-instruct": {"input": 0.25, "output": 0.75},
}

def estimate_cost(model, prompt_tokens, completion_tokens):
    pricing = MODEL_PRICING.get(model, {"input": 1.00, "output": 2.00})
    input_cost = (prompt_tokens / 1_000_000) * pricing["input"]
    output_cost = (completion_tokens / 1_000_000) * pricing["output"]
    return round(input_cost + output_cost, 8)


def call_openrouter(model, prompt, system_prompt=None, temperature=0.7, max_tokens=4096):
    if not API_KEY:
        return {"error": "OPENROUTER_API_KEY not set in environment"}

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }).encode()

    req = Request(f"{BASE_URL}/chat/completions", data=payload,
                  headers={
                      "Authorization": f"Bearer {API_KEY}",
                      "Content-Type": "application/json",
                      "HTTP-Referer": "https://hearthandcode.dev",
                      "X-Title": "Hearth & Code Curriculum Generator",
                  })

    try:
        resp = urlopen(req, timeout=120)
        data = json.loads(resp.read())
        choice = data["choices"][0]
        usage = data.get("usage", {})
        pt = usage.get("prompt_tokens", 0)
        ct = usage.get("completion_tokens", 0)
        model_used = data.get("model", model)

        return {
            "result": choice["message"]["content"],
            "model": model_used,
            "usage": {
                "prompt_tokens": pt,
                "completion_tokens": ct,
                "total_tokens": pt + ct,
            },
            "cost_usd": estimate_cost(model, pt, ct),
            "stop_reason": choice.get("finish_reason", "unknown"),
        }
    except URLError as e:
        return {"error": f"API call failed: {e}"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def list_models():
    """Return the list of supported models with pricing."""
    return {
        model: {"input_per_1m": pricing["input"], "output_per_1m": pricing["output"]}
        for model, pricing in sorted(MODEL_PRICING.items())
    }


def main():
    parser = argparse.ArgumentParser(description="OpenRouter API Wrapper")
    parser.add_argument("--model", default="deepseek/deepseek-v4-flash",
                        help="Model to use (e.g., anthropic/claude-sonnet-4)")
    parser.add_argument("--prompt", help="The prompt to send")
    parser.add_argument("--system", help="System prompt (optional)")
    parser.add_argument("--temp", type=float, default=0.7, help="Temperature (0.0-1.0)")
    parser.add_argument("--max-tokens", type=int, default=4096, help="Max output tokens")
    parser.add_argument("--list-models", action="store_true", help="List available models")
    parser.add_argument("--module", help="Module ID for cost tracking (e.g., M01)")
    parser.add_argument("--section", help="Section name for cost tracking")

    args = parser.parse_args()

    if args.list_models:
        print(json.dumps(list_models(), indent=2))
        return

    # Read prompt from arg or stdin
    prompt = args.prompt
    if not prompt and not sys.stdin.isatty():
        prompt = sys.stdin.read().strip()
    if not prompt:
        parser.print_help()
        sys.exit(1)

    result = call_openrouter(args.model, prompt, args.system, args.temp, args.max_tokens)

    if "error" in result:
        print(json.dumps(result))
        sys.exit(1)

    # Append usage info
    output = {
        "result": result["result"],
        "metadata": {
            "model": result["model"],
            "usage": result["usage"],
            "cost_usd": result["cost_usd"],
            "stop_reason": result["stop_reason"],
        }
    }

    # Optional cost log entry
    log_entry = {}
    if args.module and args.section:
        log_path = os.path.expanduser("~/devel/hearthandcode/internal/hearthandcode-hub/cost-tracking/usage.csv")
        import csv
        log_entry = [datetime.now().isoformat(), result["model"], args.module, args.section,
                     "openrouter-wrapper", result["usage"]["prompt_tokens"],
                     result["usage"]["completion_tokens"], result["usage"]["total_tokens"],
                     result["cost_usd"] * 0.3, result["cost_usd"] * 0.7, result["cost_usd"], ""]
        exists = os.path.exists(log_path)
        with open(log_path, "a", newline="") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(["timestamp","model","module","section","task",
                                 "prompt_tokens","completion_tokens","total_tokens",
                                 "input_cost","output_cost","total_cost","session_id"])
            writer.writerow(log_entry)

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()