# 🐣 Setup Guide (Hindi + English)

Dono tools (prompt enhancer + video generation) free hain. Neeche step-by-step.

---

## Part A: Prompt Enhancer (MiniMax H3)

### Option 1: Local — Ollama (100% free, no API key)

1. Install [Ollama](https://ollama.com/download) (Windows)
2. Model download karo:
   ```bash
   ollama pull qwen2.5:32b
   # ya chhota (fast but kam quality): ollama pull qwen2.5:14b
   ```
3. Enhancer chalao:
   ```bash
   python scripts/h3_prompt_enhancer.py --ollama --model qwen2.5:32b --prompt "A woman walking down a neon corridor"
   ```

### Option 2: Free API — Groq (fast, free tier)

1. [Groq](https://console.groq.com) pe free account banao
2. **API Key** copy karo
3. Chalao:
   ```bash
   set H3_API_KEY=your_groq_key
   python scripts/h3_prompt_enhancer.py --api https://api.groq.com/openai/v1 --model llama-3.3-70b-versatile --prompt "your idea"
   ```

---

## Part B: Video generation (free, Kaggle)

1. [Kaggle](https://www.kaggle.com) pe account banao (phone verify karna padta hai)
2. `notebooks/ltx_video_kaggle.ipynb` download karo
3. Kaggle → **Code → New Notebook → File → Import Notebook** → upload
4. Right sidebar → **Session options → Accelerator → GPU T4 x2** + **Internet ON**
5. Run all cells
   - **Step 3** = text-to-video (prompt likho)
   - **Step 4** = image-to-video (portrait upload karo — **faces ke liye best**)
6. Output `outputs/` me milega, download karo

> 💡 Notes:
> - Kaggle free me rozana ~30 hrs GPU time milta hai
> - Quality ke liye prompt enhancer ka brief use karo (Part A)
> - LTX-2.5 (naya, audio+video) ke liye https://github.com/Lightricks/LTX-2 dekho

---

## Part C: Troubleshooting

| Problem | Solution |
|---|---|
| Kaggle me `Internet OFF` | Settings se Internet ON karo |
| GPU time khatam | Agle din wait karo (daily reset) |
| Notebook error | Repo ke Issues me daalo, ya README ke links |
| Enhancer me `HTTP 401` | API key galat hai — dobara copy karo |
| Ollama slow | Chhota model use karo (qwen2.5:14b) |
