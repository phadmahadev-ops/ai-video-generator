# 🖥️ Local PC Setup — GPU ke hisaab se (video generation)

Ye guide batati hai **aapke GPU pe kaunsa model chalega**, kitna **system RAM**
chahiye, aur **setup** kaise karna hai. (Data: HF trending, Nov 2026)

---

## 1. GPU Tier — kaunsa model, kitna RAM

| Tier | GPU (VRAM) | Best model(s) | System RAM zaroori |
|---|---|---|---|
| 🟥 4GB | GTX 1650 (laptop) | ❌ video gen recommended nahi — **cloud use karo** (Kaggle/Colab) | 16GB |
| 🟧 6–8GB | GTX 1660 Ti / RTX 3050/3060 | Wan2.1-1.3B · LTX 2B distilled (fp8) · FastFrames-S | 16GB |
| 🟨 10–12GB | RTX 3060 12GB / 4060 Ti | Wan2.2-5B (fast) · LTX 2B full · FastFrames-L | 16–32GB |
| 🟩 16GB | RTX 4070 / 4080 | Wan2.2-5B full · HunyuanVideo (480p) · Wan2.1-14B (quantized) | 32GB |
| 🟦 24GB | RTX 4090 / 5090 / A5000 | **MiniMax H3** · **LTX-2.5** · Sulphur-2 · Wan2.2-A14B · HunyuanVideo (720p) | 32–64GB |
| 🟪 48GB+ | A6000 / A100 / multi-GPU | Sab kuch (4K bhi) | 64GB+ |

> 💡 **Best GPU (price/quality):** RTX 4090 (24GB) — H3 + LTX-2.5 dono
> full quality me. Lower budget: **RTX 3060 12GB** — Wan2.2-5B.
> Laptop 4GB: cloud hi use karo.

---

## 2. Models + setup (per model)

### Wan2.1-1.3B — minimum (6–8GB VRAM)
- Link: https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B
- Setup (ComfyUI): ComfyUI me `ComfyUI-WanVideoWrapper` custom node install karo
  (https://github.com/kijai/ComfyUI-WanVideoWrapper), model `models/diffusion_models/` me daalo.
- RAM: 16GB system RAM.
- Res: 480p tak, fast.

### LTX-Video 2B distilled — minimum (8GB VRAM)
- Link: https://huggingface.co/Lightricks/LTX-Video (`ltxv-2b-0.9.8-distilled`)
- Setup (official CLI):
  ```bash
  git clone https://github.com/Lightricks/LTX-Video.git && cd LTX-Video
  pip install -e ".[inference]"
  python inference.py --prompt "aapka prompt" \
      --pipeline_config configs/ltxv-2b-0.9.8-distilled.yaml \
      --height 512 --width 768 --num_frames 121 --seed 42
  ```
- Ya ComfyUI: `ComfyUI-LTXVideo` (https://github.com/Lightricks/ComfyUI-LTXVideo)
- RAM: 16GB. Res: 768x512 tak.

### FastFrames-S/L (Apple) — 8GB / 16GB
- Link: https://huggingface.co/apple/FastFrames-S | https://huggingface.co/apple/FastFrames-L
- Setup: HF model page pe `Use in diffusers`/demo link follow karo (naya, Nov 2026).
- RAM: 16GB (S) / 32GB (L).

### Wan2.2-5B — mid (12GB VRAM)
- Link: https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B / `Wan2.2-T2V-5B`
- Setup (ComfyUI): `ComfyUI-WanVideoWrapper` + `Wan2.2` text encoder + VAE
  (ComfyUI example workflows: https://github.com/Comfy-Org/ComfyUI_examples)
- RAM: 16–32GB. Res: 720p tak, fast.

### HunyuanVideo — high (16–24GB VRAM)
- Link: https://huggingface.co/tencent/HunyuanVideo
- Setup: official repo https://github.com/Tencent/HunyuanVideo
  ```bash
  git clone https://github.com/Tencent/HunyuanVideo.git && cd HunyuanVideo
  pip install -r requirements.txt
  python sample_t2v.py --prompt "..." --model 13B
  ```
- RAM: 32GB. Res: 720p (24GB) / 480p (16GB quantized).

### MiniMax H3 — best (24GB VRAM)
- Link: https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora
- Setup (ComfyUI): `drbaph/MiniMax-H3-Turbo-Lora-ComfyUI`
  (https://huggingface.co/drbaph/MiniMax-H3-Turbo-Lora-ComfyUI)
- Ya Kaggle (free T4 x2): hamara notebook `notebooks/minimax_h3_kaggle.ipynb`
- RAM: 32GB+. Video+audio, lip sync, ref→video, 4-step.

### LTX-2.5 — best (24GB VRAM)
- Link: https://github.com/Lightricks/LTX-2 (weights: Lightricks/LTX-2.5-Diffusers)
- Setup: official repo README follow karo (gradio app included).
- RAM: 32–64GB. Audio+video native, multi-shot.

### Sulphur-2-base — best (24GB VRAM)
- Link: https://huggingface.co/SulphurAI/Sulphur-2-base
- Setup: HF model page ka `Use in diffusers`/demo.
- RAM: 32GB.

---

## 3. General local setup checklist

1. Python 3.10–3.12 (3.13 se kuch libs issue kar sakti hain)
2. PyTorch CUDA: `pip install torch --index-url https://download.pytorch.org/whl/cu130`
3. NVIDIA driver latest (Game Ready/Studio)
4. ComfyUI (recommended): https://github.com/comfyanonymous/ComfyUI
   - `ComfyUI-WanVideoWrapper` (Wan)
   - `ComfyUI-LTXVideo` (LTX)
   - H3 LoRA pack (upar)
5. Disk: models 5–40GB + cache

## 4. Aapka GPU (GTX 1650 4GB) — kya karein?

- Video **generation** local me recommended nahi (VRAM kam hai).
- Use: **cloud free** — Kaggle T4 x2 (H3) ya Colab T4 (LTX).
- Local me video **enhance** karo (hamara `video-enhance` repo — 4GB chal jata hai).
