# Indian Mom vs Mobile Phone

A separate project folder for a 50-second Hindi 2D-cartoon YouTube Short.

## Output
- MP4, vertical 9:16 (1080x1920), 24 fps
- Exactly 50 seconds (five 10-second scenes)
- Colorful original vector-style cartoon scenes
- Hindi narration via Google Text-to-Speech (gTTS)

## Render on GitHub
1. Open the repository's **Actions** tab.
2. Select **Render Indian Mom Short**.
3. Click **Run workflow**.
4. When it finishes, open the run and download the artifact named `indian-mom-vs-mobile-phone-50s`.

The workflow also runs automatically when files in this folder or its workflow are pushed to `main`.

## Edit
Change the scene text and dialogue in `video/generate.py`, then commit. The workflow will render a fresh MP4.
