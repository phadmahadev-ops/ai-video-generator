# ⚡ Quickstart (1-page)

## Video banana hai (free)

| Kaun | Kya kare |
|---|---|
| **Quality #1** | Kaggle → `MiniMax H3` notebook → Copy & Edit → GPU T4 x2 → Run all → UI link |
| **Sabse fast** | Colab → `LTX` notebook → Run all → prompt likho |
| **Face chahiye** | Image-to-video + portrait (LTX Step 4 / H3 `fused`) |
| **Hindi prompt** | English me likho (H3 dialogue: 11 languages, Hindi nahi) |

## Prompt enhancer

```
# Ollama (local free):
python scripts/h3_prompt_enhancer.py --ollama --model qwen2.5:32b --prompt "your idea"

# Groq (free tier):
set H3_API_KEY=gsk_...
python scripts/h3_prompt_enhancer.py --api https://api.groq.com/openai/v1 --model llama-3.3-70b-versatile --prompt "your idea"
```

Output = brief → paste into H3 / LTX prompt box.

## UI

```
pip install -r requirements-ui.txt
python ui/model_hub_ui.py     # ya ui\launch_ui.bat
```

## Links

- Kaggle: https://www.kaggle.com
- Colab: https://colab.research.google.com
- Models/ratings: docs/MODEL_LEADERBOARD.md
- Setup detail: docs/SETUP_GUIDE.md
