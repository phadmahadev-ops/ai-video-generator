# 🎥 ai-video-generator

Free AI video generation (text/image-to-video) with **high face accuracy and
human realism**, plus the **MiniMax H3 prompt enhancer** to get studio-grade
prompt briefs.

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

## 🧠 Best free models for realistic faces (Nov 2026)

| Model | Free? | GPU needed | Face/human realism | Notes |
|---|---|---|---|---|
| **LTX-2.5** (22B, distilled INT8) | ✅ weights, run on Kaggle T4 x2 | T4 x2 / 24GB | Very high | Audio+video sync, multi-shot; https://github.com/Lightricks/LTX-2 |
| **LTX-Video** 13B/2B distilled | ✅ open | T4 (2B) / 24GB (13B) | High | Simple CLI (this repo's notebook); i2v with reference portrait |
| **MiniMax H3** | ✅ weights | RTX 4090/24GB+ (or Kaggle T4 x2 INT8) | Very high | Use `h3_prompt_enhancer.py` for best results; audio+video |
| **Wan 2.2** | ✅ open | 24GB | High | Long videos, good human motion |
| HunyuanVideo | ✅ open | 24GB+ | Medium-high | Good general quality, heavier |

> Face accuracy tips: always use **image-to-video with a reference portrait**
> (don't generate a face from text alone), keep the same seed, and describe
> the person with identical wording in every prompt.

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

## ⚖️ License

Code: MIT (see [LICENSE](LICENSE)). Model weights keep their own licenses
(LTX: OpenRail-M/community; MiniMax H3: terms on HF; use per your use case).
The H3 system prompt is public material from a GitHub gist by Naxdy.
