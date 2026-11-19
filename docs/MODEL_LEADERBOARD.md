# 🏆 Video Model Leaderboard (free, text-to-video)

Ratings 1-5 ⭐. Data: HuggingFace trending (Nov 2026) + community reports.
"Hindi" = prompt/dialogue me Hindi kitni achhi chalti hai.

| Rank | Model | FREE | Face ⭐ | Speed ⭐ | Quality ⭐ | Hindi ⭐ | VRAM / GPU | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | **MiniMax H3** (Turbo INT8 / LoRA) | ✅ weights | 5 | 4 | 5 | 2 | T4 x2 (INT8) / 24GB | Best overall: video+audio, lip-sync, ref→video, 4-step. [HF](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora) [Kaggle](https://www.kaggle.com/code/gattootv/minimax-h3-turbo-int8-video-audio-reuploaded) |
| 2 | **LTX-2.5** (22B distilled) | ✅ weights | 5 | 4 | 4.5 | 2 | T4 x2 / 24GB | Native audio+video, multi-shot, great faces. [HF](https://huggingface.co/Lightricks/LTX-2.5-Diffusers) [Repo](https://github.com/Lightricks/LTX-2) |
| 3 | **Sulphur-2-base** | ✅ | 4.5 | 3.5 | 4.5 | 1 | 24GB | Fast-growing, 96K downloads, 2.2K likes. [HF](https://huggingface.co/SulphurAI/Sulphur-2-base) |
| 4 | **Wan2.1/2.2 T2V** (14B/5B) | ✅ weights | 4 | 4 | 4 | 1 | 24GB (14B) / 12GB (5B) | Very popular, solid humans/motion. [HF](https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B) |
| 5 | **HunyuanVideo** | ✅ weights | 3.5 | 3 | 4 | 1 | 24GB+ | Tencent, good scenes, faces ok. [HF](https://huggingface.co/tencent/HunyuanVideo) |
| 6 | **LTX-Video 2B distilled** (legacy) | ✅ | 3.5 | 5 | 3.5 | 2 | T4 (single) | Fastest free on T4; good for quick drafts. [HF](https://huggingface.co/Lightricks/LTX-Video) |
| 7 | **Wan2.1-1.3B** | ✅ | 3 | 5 | 3 | 1 | 8GB | Very light, creative, low fidelity. |
| 8 | **FastFrames-L/S** (Apple) | ✅ | 3.5 | 5 | 3.5 | 1 | 16GB/8GB | New (Nov 2026), speed-focused. [HF](https://huggingface.co/apple/FastFrames-L) |
| 9 | **LongCat-Video** | ✅ | 4 | 3 | 4 | 1 | 24GB | Avatars/talking heads. [HF](https://huggingface.co/meituan-longcat/LongCat-Video) |

## 🧑 Face accuracy specials

| Model | Use for | Link |
|---|---|---|
| `Alissonerdx/LTX-Best-Face-ID` | Best face identity preservation (LTX) | https://huggingface.co/Alissonerdx/LTX-Best-Face-ID |
| `smhfacct/Minimax-H3-fl2va-ref2va-hybrid-models` | H3 face-hybrid | https://huggingface.co/smhfacct/Minimax-H3-fl2va-ref2va-hybrid-models |
| `NicoLab28/ClipProj-MiniMax-H3` | Better image conditioning for H3 | https://huggingface.co/NicoLab28/ClipProj-MiniMax-H3 |

> Tip: faces ke liye hamesha **image-to-video with reference portrait** — pure text face mat banao.

## 🌐 Language / Hindi support

- **MiniMax H3** dialogue: 11 languages (Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish) — **Hindi nahi**.
- **Hindi prompt** ke liye: prompt English me likho, ya translation use karo (model kuch Hindi samajh sakte hain, par guarantee nahi).
- Sabse achhi Hindi: koi bhi model + **English prompt** (result ek jaisa), ya local TTS (e.g. IndicF5) se audio dub karo.

## ⚡ Fastest setup per GPU

| GPU | Best choice |
|---|---|
| T4 x2 (Kaggle free) | MiniMax H3 INT8 (Kaggle notebook) ya LTX-2.5 |
| 24GB (4090) | MiniMax H3 bf16 / LTX-2.5 / Sulphur-2 |
| 16GB | Wan2.2-5B / FastFrames-L / LTX 2B distilled |
| 8GB | Wan2.1-1.3B / LTX 2B (fp8) |
