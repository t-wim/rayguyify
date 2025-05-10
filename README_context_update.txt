### Context‑based template upgrade

**Replace / remove:**
1. Delete old `topics.json` and copy the new one provided here.
2. Replace your existing `meme_generator.py` with the new version in this package.
3. You no longer need any `emo_*.png` overlay images; only keep `base_raycast.png` inside `templates/`.
4. No changes required in `bot.py`.

The new generator adds a colored tint, big headline (topic name), and caption
generated on the fly, using the descriptive default captions from `topics.json`.
