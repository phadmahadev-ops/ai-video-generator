# Prompt Examples (MiniMax H3 / LTX)

Raw prompt daalo `h3_prompt_enhancer.py` me — **enhanced brief** nikalega.
Neeche 3 examples hain: raw → jaisa output aata hai.

---

## Example 1: T2VA (text only)

**Raw:**
```
A woman walking down a neon corridor, camera tracking back, no background music
```

**Enhanced (brief):**
```
integrated_multimodal_description: [Shot 1] Cinematic, live-action, medium-wide
tracking shot. A woman in her late 20s with long red hair and blue eyes walks
toward the camera down a narrow sci-fi corridor with hexagonal black metallic
walls and red neon strips. She wears a black tactical undersuit. The camera
pulls back at medium amplitude, matching her pace. At 00:02.000, thin red
laser beams flicker and lock onto her body. At 00:04.000, glowing red
holographic wireframes envelop her limbs and torso, then solid black armor
plates with glowing red circuitry materialize from the boots upward. At
00:08.000, the helmet snaps shut with an orange visor glowing. She stops and
stands perfectly still as the shot ends.

overall_soundscape: Rhythmic metallic boot-steps echoing against corridor
walls, a low-frequency industrial hum, high-pitched electronic chirps from
the lasers, a digital shimmer as wireframes appear, and heavy mechanical
clunks as armor plates lock into place.

non_diegetic_music: N/A
```

---

## Example 2: T2VA (cinematic, with dialogue)

**Raw:**
```
A captain on a starship bridge sees a fleet jump to hyperspace, she is shocked
```

**Enhanced body (extract):**
```
[Shot 1] Cinematic, medium wide shot, pushing in slowly. In the cavernous,
dimly lit bridge of a starship, a female captain in her late 40s with an
athletic build and short silver-streaked black hair stands centered, wearing
a structured high-collared dark navy military tunic. Her back is to the
camera, silhouetted against cool ambient starlight. Outside, a massive armada
of jagged grey dreadnoughts hovers in tight formation against a deep purple
nebula. The fleet's rear thrusters begin to glow with intense escalating blue
light. [Shot 2] At 00:04.500, the camera cuts to a close-up of her face and
shakes strongly. A blinding white flash floods through the window as the
fleet jumps to hyperspace. She staggers forward, braces herself, then slowly
closes her eyes in the newly emptied space.
```

---

## Example 3: Full-reference (image-to-video, face accuracy)

Use jab portrait image ho (face consistency ke liye best):

**Raw:**
```
The woman from <Picture 1> is walking down the corridor in <Picture 3>,
facing the camera. Red laser beams target her and the suit from <Picture 2>
materializes around her. One continuous shot. No background music.
```

**Enhanced:**
```
subject_definitions:
<Subject 1>: The woman from <Picture 1>, characterized by long red hair, blue
eyes, and a determined expression, initially wearing a black tactical undersuit.
<Subject 2>: The futuristic armored suit from <Picture 2>, matte black plating,
glowing red circuitry accents, and a helmet with a translucent orange visor.
<Subject 3>: The sci-fi corridor from <Picture 3>, hexagonal black metallic
wall panels with red neon lighting and white ceiling strips.
<Picture 1>: Reference for facial features and initial attire of <Subject 1>.
<Picture 2>: Reference for the geometry/appearance of the final armor.
<Picture 3>: Reference for the environment and lighting of the scene.

summary:
[reference generation] A continuous tracking shot of <Subject 1> walking
through <Subject 3> while being enveloped by a materializing armor.

retention_analysis:
<Subject 1>: fully_preserved - facial identity and red hair maintained until
the helmet closes.
<Subject 2>: fully_preserved - final materialized armor matches <Picture 2>.
<Subject 3>: fully_preserved - corridor architecture/lighting match <Picture 3>.

detailed_description:
The target video is a high-fidelity, cinematic 3D CG sequence with sharp
textures and high-contrast lighting. [Shot 1] The scene opens with <Subject 1>
walking forward down the center of the corridor, facing the camera, dressed in
the sleek black tactical suit from <Picture 1>. The camera pulls out with
medium amplitude at a steady speed matching her pace. At 02.000, thin sharp
red laser beams appear from the periphery, flickering as they lock onto her.
At 04.000, glowing red holographic wireframes mirroring <Subject 2> snap into
existence around her. From 06.000 to 08.000, solid black metallic plates and
red glowing strips rapidly materialize from the boots upward in a fluid
digital growth effect. The shot concludes at 08.000 as the heavy armor helmet
snaps shut, orange visor glowing.

overall_soundscape: Rhythmic metallic boot-steps, low-frequency industrial
hum, electronic chirps from lasers, digital shimmering as wireframes appear,
heavy mechanical clunks and pneumatic hisses as armor locks into place.

non_diegetic_music: N/A
```

---

## Tips

- **Faces:** hamesha `<Picture N>` reference use karo (text se face mat banao).
- **No music chahiye?** Last me `No background music.` likho (enhancer ise N/A bana dega).
- **Dialogue:** `[English] ...` tags use karo (H3 11 languages support karta hai).
- **Camera:** hamesha batao — `static shot`, `push in`, `pan left`, etc.
