# 🎥 ai-video-generator

Free AI video generation (text/image-to-video) with **high face accuracy and
human realism**, plus the **MiniMax H3 prompt enhancer** to get studio-grade
prompt briefs.

[![MIT](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![Contributing](https://img.shields.io/badge/contributions-welcome-orange)](CONTRIBUTING.md)
[![Quickstart](https://img.shields.io/badge/Quickstart-1page-purple)](docs/QUICKSTART.md)
[![Local Setup](https://img.shields.io/badge/Local-GPU_guide-teal)](docs/LOCAL_SETUP.md)

| Badge | Kaun use kare |
|---|---|
| [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/phadmahadev-ops/ai-video-generator/blob/main/notebooks/ltx_video_kaggle.ipynb) | LTX video generation — Colab/T4 pe directly |
| [![Kaggle](https://img.shields.io/badge/kaggle-%2320BEFF.svg?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com) | Notebook import karke T4 GPU pe chalao |
| [![Setup Guide](https://img.shields.io/badge/Setup-Guide-blue)](docs/SETUP_GUIDE.md) | Naye users ke liye step-by-step |
| [![Prompt Examples](https://img.shields.io/badge/Examples-Prompts-orange)](examples/prompt_examples.md) | Ready-made raw → enhanced pairs |


## 📦 What's inside

| File | Purpose |
|---|---|
| `scripts/h3_prompt_enhancer.py` | Turns a raw idea into a detail-rich MiniMax H3 "production brief" (T2VA / full-reference). Works with any OpenAI-compatible LLM API (Ollama, Groq, OpenRouter, vLLM, LM Studio...). |
| `scripts/h3_sysprompt.md` | The H3 system prompt (source: Naxdy gist) used by the enhancer. |
| `notebooks/ltx_video_kaggle.ipynb` | Free text-to-video / image-to-video on Kaggle T4 (LTX-Video 2B distilled). Image-to-video keeps a person's face/identity. |
| `notebooks/colab_prompt_enhancer.ipynb` | Use the prompt enhancer inside Colab before generating. |

## 🧠 Best free models for realistic faces — Leaderboard (Nov 2026)

Full ratings table: [docs/MODEL_LEADERBOARD.md](docs/MODEL_LEADERBOARD.md)

| Rank | Model | Face | Speed | Quality | Hindi | Kaggle | Colab |
|---|---|---|---|---|---|---|---|
| 1 | **MiniMax H3** (Turbo INT8) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | [Open](https://www.kaggle.com/code/gattootv/minimax-h3-turbo-int8-video-audio-reuploaded) | — |
| 2 | **LTX-2.5** (22B distilled) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐½ | ⭐⭐ | [Search](https://www.kaggle.com/code?search=LTX-2.5) | — |
| 3 | **Sulphur-2-base** | ⭐⭐⭐⭐½ | ⭐⭐⭐½ | ⭐⭐⭐⭐½ | ⭐ | [Search](https://www.kaggle.com/code?search=Sulphur-2) | — |
| 4 | **Wan2.2/2.1** (14B/5B) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ | [Search](https://www.kaggle.com/code?search=Wan+2.2) | — |
| 5 | **HunyuanVideo** | ⭐⭐⭐½ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐ | [Search](https://www.kaggle.com/code?search=HunyuanVideo) | — |
| 6 | **LTX-Video 2B distilled** | ⭐⭐⭐½ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐½ | ⭐⭐ | [Import](https://raw.githubusercontent.com/phadmahadev-ops/ai-video-generator/main/notebooks/ltx_video_kaggle.ipynb) | [Open](https://colab.research.google.com/github/phadmahadev-ops/ai-video-generator/blob/main/notebooks/ltx_video_kaggle.ipynb) |

> Kaggle link click karo → notebook page khulegi (login sirf run pe).
> Colab link bina login khulta hai. Ban rating: docs/MODEL_LEADERBOARD.md

> Face accuracy tips: always use **image-to-video with a reference portrait**
> (don't generate a face from text alone), keep the same seed, and describe
> the person with identical wording in every prompt. Hindi dialogue: H3
> supports 11 languages (Hindi nahi) — English prompt likho ya TTS dub karo.

## 🖥️ Local PC (apne GPU pe) — GPU ke hisaab se

Full guide + setup: [docs/LOCAL_SETUP.md](docs/LOCAL_SETUP.md)

| Aapka GPU (VRAM) | Best model | System RAM |
|---|---|---|
| 4GB (laptop) | ❌ cloud use karo (Kaggle/Colab) | 16GB |
| 6–8GB | Wan2.1-1.3B · LTX 2B distilled · FastFrames-S | 16GB |
| 10–12GB | Wan2.2-5B · LTX 2B full · FastFrames-L | 16–32GB |
| 16GB | Wan2.2-5B full · HunyuanVideo 480p | 32GB |
| **24GB** | **MiniMax H3** · **LTX-2.5** · Sulphur-2 · Wan14B | 32–64GB |

> 💡 Best GPU: **RTX 4090 (24GB)** · Budget: **RTX 3060 12GB**.
> Aapka GTX 1650 4GB: generation cloud pe, enhance local (`video-enhance` repo).

## 🎛️ Model Hub UI (rated cards + prompt enhancer)

```bash
pip install -r requirements-ui.txt
python ui/model_hub_ui.py      # ya: ui\launch_ui.bat
```

Open http://127.0.0.1:7860 — rated model cards, one-click links, aur
built-in H3 prompt enhancer (raw idea → brief).

## 🚀 Prompt enhancer (MiniMax H3)

```bash
# local, free (Ollama)
python scripts/h3_prompt_enhancer.py --ollama \
    --model llama3.1:70b \
    --prompt "A woman walking down a neon corridor, camera tracking back"

# any OpenAI-compatible API
set H3_API_KEY=sk-...
python scripts/h3_prompt_enhancer.py \
    --api https://api.groq.com/openai/v1 \
    --model llama-3.3-70b-versatile \
    --prompt "A man on a rooftop at sunset, wind in his hair"
```

Output = only the brief text. Paste it into MiniMax H3 (or use it as the
prompt template for any video model — LTX also benefits from structured
prompts).

## 🚀 Generate video (free, Kaggle T4)

### 📚 Notebooks

| Notebook | Kya hai | Status | Colab | Kaggle |
|---|---|---|---|---|
| `ltx_video_kaggle.ipynb` | Free text/image-to-video (realistic faces) | ✅ working (Nov 2026) | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/phadmahadev-ops/ai-video-generator/blob/main/notebooks/ltx_video_kaggle.ipynb) | [![Download for Kaggle](https://img.shields.io/badge/Download-Kaggle-20BEFF)](https://raw.githubusercontent.com/phadmahadev-ops/ai-video-generator/main/notebooks/ltx_video_kaggle.ipynb) |
| `colab_prompt_enhancer.ipynb` | H3 prompt enhancer (Colab, needs API key) | ✅ working (Nov 2026) | [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/phadmahadev-ops/ai-video-generator/blob/main/notebooks/colab_prompt_enhancer.ipynb) | — |
| `minimax_h3_kaggle.ipynb` | MiniMax H3 Turbo INT8 — text/image/reference→video + audio, 4-step PDMD/DMAD/fused (T4 x2) | ✅ working (Nov 2026) | — | [![Open on Kaggle](https://img.shields.io/badge/Open-Kaggle-20BEFF)](https://www.kaggle.com/code/gattootv/minimax-h3-turbo-int8-video-audio-reuploaded) |

## 🔗 Direct Kaggle links

```
# Original (public, 236 upvotes):
Kaggle Notebook : https://www.kaggle.com/code/gattootv/minimax-h3-turbo-int8-video-audio-reuploaded

# Aapka copy (fork, mahadevfebfeb):
Kaggle Notebook : https://www.kaggle.com/code/mahadevfebfeb/minimax-h3-turbo-int8-video-audio-reu-b1845d
```

Login tabhi mangta hai jab run karna ho (Copy & Edit). Link khulne ke liye bas
click karo — khulega.

> Attribution: `minimax_h3_kaggle.ipynb` is a public re-upload of the AIQUEST Academy H3 notebook (by *Gattoo TV*, [Kaggle](https://www.kaggle.com/code/gattootv/minimax-h3-turbo-int8-video-audio-reuploaded), 236 upvotes). Downloaded for convenience; run it from our repo or directly on Kaggle.

### Steps (Kaggle)

1. **Download for Kaggle** button dabao (raw `.ipynb` download hoga)
2. [kaggle.com](https://www.kaggle.com) → Sign in (free)
3. Code → New Notebook → **File → Import Notebook** → download hui file upload karo
4. Right panel → Settings → Accelerator → **GPU T4 x2**; Internet → **ON**
5. Run all cells. For faces use **Step 4 (image-to-video)** with your portrait.

Full beginner setup: [docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md) (Hindi+English)

## 🔗 Related / inspiration

- [TeamAIQ/Colab-notebooks](https://github.com/TeamAIQ/Colab-notebooks) — notebook collection (idea source)
- [TeamAIQ/h3-lora-comparison](https://github.com/TeamAIQ/h3-lora-comparison) — MiniMax H3 LoRA (PDMD/DMAD/Fused turbo) speed-quality comparison
- [MiniMax H3 Turbo INT8 (Kaggle original)](https://www.kaggle.com/code/gattootv/minimax-h3-turbo-int8-video-audio-reuploaded) — source of our H3 notebook copy

## ⚖️ License

Code: MIT (see [LICENSE](LICENSE)). Model weights keep their own licenses
(LTX: OpenRail-M/community; MiniMax H3: terms on HF; use per your use case).
The H3 system prompt is public material from a GitHub gist by Naxdy.
