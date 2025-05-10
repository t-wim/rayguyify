
import os, json, uuid, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
OUT = ROOT / "generated"
OUT.mkdir(exist_ok=True)

TOPICS = json.load(open(ROOT / "topics.json"))

def generate(topic: str, caption: str = "") -> str:
    if topic not in TOPICS:
        topic = list(TOPICS)[0]
    info = TOPICS[topic]

    base = Image.open(TEMPLATES / "base_raycast.png").convert("RGBA")

    # dynamic overlay: slight color tint per topic
    tint = {
        "fomo": (255,255,0,80),
        "degen": (255,0,255,80),
        "copium": (0,255,255,80),
        "diamond_hands": (0,255,0,60),
        "jeet": (255,128,0,80),
        "rekt": (255,0,0,100),
        "rugpull": (255,0,0,120),
        "holding": (0,128,255,60),
        "valhalla": (128,0,255,80),
        "wagmi": (0,255,128,60)
    }.get(topic, (255,255,255,0))

    color_layer = Image.new("RGBA", base.size, tint)
    img = Image.alpha_composite(base, color_layer)

    draw = ImageDraw.Draw(img)
    try:
        title_font = ImageFont.truetype("arial.ttf", 160)
        text_font  = ImageFont.truetype("arial.ttf", 48)
    except:
        title_font = ImageFont.load_default()
        text_font  = ImageFont.load_default()

    # Big headline (topic)
    title = topic.upper()
    tw, th = draw.textsize(title, font=title_font)
    draw.text(((img.width-tw)//2, 60), title, font=title_font,
              fill="white", stroke_width=4, stroke_fill="black")

    # Caption logic
    if not caption:
        caption = info["default_caption"]
    wrapped = textwrap.fill(caption, 30)
    w,h = draw.multiline_textsize(wrapped, font=text_font)
    draw.multiline_text(((img.width-w)//2, img.height-h-40), wrapped,
                        font=text_font, fill="white", align="center",
                        stroke_width=2, stroke_fill="black")

    out = OUT / f"{uuid.uuid4().hex}.png"
    img.save(out)
    return str(out)

if __name__ == "__main__":
    print("Test:", generate("fomo"))
