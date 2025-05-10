# RayGuyify – Solana/Raydium Meme Reply Bot

Automatically replies to any mention on X (Twitter) with a Ray Guy meme that
matches the tweet’s sentiment (FOMO, JEET, Holding, Copium, etc.).

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in your Twitter keys
python bot.py          # local test, replies within 90 s
```

Essential (free) API tier is enough; the bot polls mentions every 90 seconds.

## Repo layout
```
.
├── bot.py                # main loop (v2 read / v1.1 upload)
├── meme_generator.py     # compositing engine
├── topics.json           # keyword → overlay mapping
├── templates/            # base image + emotion overlays
│   ├── base_raycast.png
│   └── emo_<topic>.png   # 10 overlays
├── requirements.txt
└── .env.example
```
