#!/usr/bin/env python3
"""
AI Video Model Hub UI (Gradio)

Showcases the best free text-to-video models with ratings, one-click links,
and a built-in MiniMax H3 prompt enhancer.

Run:
  pip install gradio
  python ui/model_hub_ui.py
"""

import os
import sys
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")

try:
    import gradio as gr
except ImportError:
    print("pip install gradio  (ya: pip install -r requirements-ui.txt)")
    sys.exit(1)

from h3_prompt_enhancer import load_sysprompt, call_api  # noqa: E402

MODELS = [
    {"rank": 1, "name": "MiniMax H3 (Turbo INT8)", "face": 5, "speed": 4,
     "quality": 5, "hindi": 2,
     "link": "https://www.kaggle.com/code/gattootv/minimax-h3-turbo-int8-video-audio-reuploaded",
     "note": "Best overall: video+audio, lip-sync, ref→video. T4 x2 on Kaggle."},
    {"rank": 2, "name": "LTX-2.5 (22B distilled)", "face": 5, "speed": 4,
     "quality": 4, "hindi": 2,
     "link": "https://github.com/Lightricks/LTX-2",
     "note": "Audio+video, multi-shot, great faces. 24GB / T4 x2."},
    {"rank": 3, "name": "Sulphur-2-base", "face": 4, "speed": 3,
     "quality": 4, "hindi": 1,
     "link": "https://huggingface.co/SulphurAI/Sulphur-2-base",
     "note": "Fast-growing community favorite. 24GB."},
    {"rank": 4, "name": "Wan2.2/2.1 T2V (14B/5B)", "face": 4, "speed": 4,
     "quality": 4, "hindi": 1,
     "link": "https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B",
     "note": "Very popular, solid motion. 24GB (14B) / 12GB (5B)."},
    {"rank": 5, "name": "HunyuanVideo", "face": 3, "speed": 3,
     "quality": 4, "hindi": 1,
     "link": "https://huggingface.co/tencent/HunyuanVideo",
     "note": "Tencent, good scenes. 24GB+."},
    {"rank": 6, "name": "LTX-Video 2B distilled (legacy)", "face": 3,
     "speed": 5, "quality": 3, "hindi": 2,
     "link": "https://huggingface.co/Lightricks/LTX-Video",
     "note": "Fastest free on a single T4; quick drafts."},
    {"rank": 7, "name": "Wan2.1-1.3B", "face": 3, "speed": 5,
     "quality": 3, "hindi": 1,
     "link": "https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B",
     "note": "Very light (8GB)."},
    {"rank": 8, "name": "FastFrames-L/S (Apple)", "face": 3, "speed": 5,
     "quality": 3, "hindi": 1,
     "link": "https://huggingface.co/apple/FastFrames-L",
     "note": "New (Nov 2026), speed-first. 16GB/8GB."},
    {"rank": 9, "name": "LongCat-Video", "face": 4, "speed": 3,
     "quality": 4, "hindi": 1,
     "link": "https://huggingface.co/meituan-longcat/LongCat-Video",
     "note": "Talking heads/avatars. 24GB."},
]

STARS = "⭐"


def star(n):
    return STARS * n + "☆" * (5 - n)


def model_cards():
    html = ["<div style='display:flex;flex-wrap:wrap;gap:12px;'>"]
    for m in MODELS:
        html.append(
            "<div style='border:1px solid #444;border-radius:12px;padding:12px;"
            "width:300px;background:#1e1e2e;color:#eee;'>"
            f"<b>#{m['rank']} {m['name']}</b><br>"
            f"Face {star(m['face'])} · Speed {star(m['speed'])} · "
            f"Quality {star(m['quality'])} · Hindi {star(m['hindi'])}<br>"
            f"<span style='color:#aaa'>{m['note']}</span><br>"
            f"<a href='{m['link']}' target='_blank'>Open →</a>"
            "</div>")
    html.append("</div>")
    return "".join(html)


def enhance_prompt(raw, api_url, api_key, model_name):
    if not raw.strip():
        return "Pehle prompt likho."
    if not api_url.strip():
        return "API URL do (--api), ya Ollama: http://localhost:11434/v1"
    key = api_key.strip() or "ollama"
    try:
        return call_api(api_url.strip(), key, model_name.strip() or "qwen2.5:32b",
                        [{"role": "system", "content": load_sysprompt()},
                         {"role": "user", "content": raw}])
    except Exception as e:
        return "ERROR: %s" % e


def build_ui():
    with gr.Blocks(title="AI Video Model Hub",
                    css="footer{display:none!important}") as demo:
        gr.Markdown("# 🎥 AI Video Model Hub — free text-to-video (rated)")
        gr.Markdown("Ratings: Face accuracy · Speed · Quality · Hindi support. "
                    "Details: `docs/MODEL_LEADERBOARD.md`")
        gr.HTML(model_cards())

        gr.Markdown("## ✨ MiniMax H3 Prompt Enhancer")
        with gr.Row():
            with gr.Column(scale=2):
                raw = gr.Textbox(label="Raw idea (Hindi/English dono chalta hai)",
                                 placeholder="E.g. Ek ladki neon corridor me chal rahi hai, camera piche...",
                                 lines=4)
                api_url = gr.Textbox(label="OpenAI-compatible API URL",
                                     value=os.environ.get("H3_API_URL", ""),
                                     placeholder="https://api.groq.com/openai/v1 ya http://localhost:11434/v1")
                api_key = gr.Textbox(label="API key (Ollama ke liye chhodo)",
                                     value=os.environ.get("H3_API_KEY", ""),
                                     type="password")
                model_name = gr.Textbox(label="Model", value="qwen2.5:32b")
                btn = gr.Button("Enhance → Brief", variant="primary")
            with gr.Column(scale=3):
                out = gr.Textbox(label="Enhanced brief (MiniMax H3 / LTX ready)",
                                 lines=14)
        btn.click(enhance_prompt, [raw, api_url, api_key, model_name], out)

        gr.Markdown("### 🧑 Face accuracy tip\n"
                    "Image-to-video + reference portrait use karo — text se face "
                    "mat banao. H3 ke liye `fused` variant (voice clone).")
    return demo


if __name__ == "__main__":
    demo = build_ui()
    demo.launch(inbrowser=True)
