#!/usr/bin/env python3
"""
h3_prompt_enhancer.py - MiniMax H3 prompt enhancer.

Loads the H3 system prompt (h3_sysprompt.md) and sends your raw creative
request to any OpenAI-compatible chat API (Ollama local, Groq, OpenRouter,
vLLM, LM Studio, etc.). Prints ONLY the enhanced "production brief" text.

Examples:
  # Ollama (local, free):
  python h3_prompt_enhancer.py --ollama --model llama3.1:70b \
      --prompt "A woman walking down a neon corridor, camera tracking back"

  # OpenAI-compatible API:
  set H3_API_KEY=sk-...
  python h3_prompt_enhancer.py --api https://api.groq.com/openai/v1 \
      --model llama-3.3-70b-versatile \
      --prompt "A man on a rooftop at sunset, wind in his hair"

  # Pipe from file:
  type prompt.txt | python h3_prompt_enhancer.py --ollama --model qwen2.5:32b
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
SYSPROMPT_PATH = os.path.join(HERE, "h3_sysprompt.md")


def load_sysprompt():
    with open(SYSPROMPT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    # strip the header lines up to the first "Role" line
    idx = text.find("Role")
    if idx != -1:
        text = text[idx:]
    return text


def read_prompt_from_stdin():
    return sys.stdin.read().strip()


def call_api(base_url, api_key, model, messages, timeout=600,
             temperature=0.7, max_tokens=4096):
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key,
        }, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.stderr.write("HTTP %s: %s\n" % (e.code, body[:500]))
        sys.exit(1)
    return data["choices"][0]["message"]["content"].strip()


def main():
    ap = argparse.ArgumentParser(description="MiniMax H3 prompt enhancer")
    ap.add_argument("--prompt", help="raw creative request (else read stdin)")
    ap.add_argument("--api", default=os.environ.get("H3_API_URL"),
                    help="OpenAI-compatible base URL")
    ap.add_argument("--key", default=os.environ.get("H3_API_KEY"),
                    help="API key")
    ap.add_argument("--model", default=os.environ.get("H3_MODEL", "qwen2.5:32b"))
    ap.add_argument("--ollama", action="store_true",
                    help="use local Ollama (http://localhost:11434/v1)")
    ap.add_argument("--out", help="write brief to file instead of stdout")
    ap.add_argument("--noenhance", action="store_true",
                    help="echo the prompt unchanged (debug)")
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--max-tokens", type=int, default=4096)
    ap.add_argument("--prompt-file", help="raw prompt file se padho")
    args = ap.parse_args()

    if args.prompt_file:
        with open(args.prompt_file, encoding="utf-8") as f:
            prompt = f.read()
    else:
        prompt = args.prompt if args.prompt else read_prompt_from_stdin()
    if not prompt:
        ap.error("no prompt given (use --prompt or pipe stdin)")

    if args.noenhance:
        out = prompt
    else:
        if args.ollama:
            api_url = "http://localhost:11434/v1"
            key = "ollama"
        else:
            api_url = args.api
            key = args.key
        if not api_url:
            ap.error("no API URL (use --api or --ollama)")
        sys.stderr.write("[*] model=%s url=%s\n" % (args.model, api_url))

        system = load_sysprompt()
        out = call_api(api_url, key or "", args.model,
                       [{"role": "system", "content": system},
                        {"role": "user", "content": prompt}],
                       temperature=args.temperature,
                       max_tokens=args.max_tokens)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
        sys.stderr.write("[*] brief written to %s\n" % args.out)
    else:
        print(out)


if __name__ == "__main__":
    main()
