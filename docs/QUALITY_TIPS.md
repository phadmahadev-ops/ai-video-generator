# ✨ Video Quality Tips (MiniMax H3 / LTX)

"Video ban gaya but quality kharab" — 90% time ye 3 cheezein hoti hain:

## 1. Prompt kamzor hai (sabse bada reason)

Raw prompt (`"A woman walking"`) se quality nahi aati. **Prompt enhancer**
use karo:

```bash
python scripts/h3_prompt_enhancer.py --ollama --model qwen2.5:32b \
    --prompt "A woman walking down a neon corridor, camera tracking back"
```

Enhanced brief paste karo H3 UI me — detail (lighting, camera, clothes,
beats) = quality.

## 2. Settings kam hain (H3 notebook)

| Setting | Default (kam) | Recommended (best) |
|---|---|---|
| Resolution | 480p | **768p** ya 832p (1080p = slow) |
| Duration | 5s | 5–8s |
| Steps | 4 (pdmd) | **8** (`H3_VARIANT = "official"`, ya `"dmad"`) |
| Model variant | pdmd | `official` (Ref2VA 8-step) quality ke liye; `fused` reference/video ke liye |

- `H3_VARIANT` Step 1 ki first line me change karo → Step 1 + Step 2 re-run.
- `official` = 8-step → detail + sharpness better (thoda slow).

## 3. Output ko upscale karo (final polish)

H3 768p output nikalne ke baad **4K/1080p upscale** karo:

- **FlashVSR+** (cloud, free): `video-enhance` repo ka notebook
  (https://github.com/phadmahadev-ops/video-enhance → notebooks)
- Ya local: `video-enhance` scripts (`python enhance.py video.mp4 hq 25`)

## Face quality

- Hamesha **image-to-video + reference portrait** (H3 `fused`)
- Seed fixed rakho (same seed = consistent)
- Face zoom scenes me `talking faces` LoRA bhi hai (dropdown me)

## General

- 4-step (pdmd) fast hai lekin `official`/`dmad` detail better dete hain.
- Motion zyada ho to `--temporal-compression 2` (H3) / short clips (5s) use karo.
- Output MP4 me audio aana chahiye — agar nahi, to UI me "Sound effects" edit karo.

## Checklist

- [ ] Prompt enhancer se brief (H3)
- [ ] 768p+
- [ ] official/dmad variant (8 steps)
- [ ] Post-upscale (FlashVSR+ / video-enhance)
- [ ] Face: reference image
