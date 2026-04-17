"""
ECヒーローズ講座画像生成スクリプト
Imagen 4.0 で29枚の画像を生成し、指定サイズにリサイズ/クロップする
"""
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

# Load API key
load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('GEMINI_API_KEY')
if not api_key:
    load_dotenv('C:/Users/user/.dev/elearnig/.env')
    api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('GEMINI_API_KEY')

if not api_key:
    print("ERROR: No API key found")
    sys.exit(1)

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

OUTPUT_DIR = Path('public/wp-assets/img/eccc/ec-heroes/curriculum')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BANNER_SIZE = (1200, 400)  # 3:1
LESSON_SIZE = (800, 500)   # 16:10


def generate_and_save(filename, prompt, target_size, aspect_ratio='16:9', retries=3):
    """Generate image with Imagen 4.0 and resize/crop to target size."""
    filepath = OUTPUT_DIR / filename
    if filepath.exists():
        print(f"  SKIP (exists): {filename}")
        return True

    for attempt in range(1, retries + 1):
        try:
            print(f"  Generating {filename} (attempt {attempt})...")
            result = client.models.generate_images(
                model='imagen-4.0-generate-001',
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio=aspect_ratio,
                    output_mime_type='image/png',
                ),
            )

            if not result.generated_images:
                print(f"  WARNING: No image returned for {filename}")
                if attempt < retries:
                    time.sleep(5)
                    continue
                return False

            img_bytes = result.generated_images[0].image.image_bytes
            img = Image.open(BytesIO(img_bytes))

            # Crop to target aspect ratio then resize
            target_w, target_h = target_size
            target_ratio = target_w / target_h
            img_w, img_h = img.size
            img_ratio = img_w / img_h

            if img_ratio > target_ratio:
                # Image is wider - crop sides
                new_w = int(img_h * target_ratio)
                left = (img_w - new_w) // 2
                img = img.crop((left, 0, left + new_w, img_h))
            elif img_ratio < target_ratio:
                # Image is taller - crop top/bottom
                new_h = int(img_w / target_ratio)
                top = (img_h - new_h) // 2
                img = img.crop((0, top, img_w, top + new_h))

            img = img.resize(target_size, Image.LANCZOS)
            img.save(filepath, 'PNG')
            size_kb = filepath.stat().st_size / 1024
            print(f"  OK: {filename} ({target_size[0]}x{target_size[1]}, {size_kb:.0f}KB)")
            return True

        except Exception as e:
            error_msg = str(e)
            print(f"  ERROR (attempt {attempt}): {error_msg}")
            if 'RESOURCE_EXHAUSTED' in error_msg or '429' in error_msg:
                wait = 30 * attempt
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif attempt < retries:
                time.sleep(5)
            else:
                return False

    return False


# === Banner images (1200x400, generate at 16:9 then crop to 3:1) ===
BANNERS = [
    (
        'banner_blue_ocean.png',
        'A majestic harbor at dawn with a large sailing ship ready to depart. '
        'Calm blue ocean, soft pink and orange sunrise sky reflecting on water. '
        'Navigation charts and compass visible on the dock. '
        'Professional, business-like atmosphere suggesting preparation and strategy. '
        'Cinematic wide angle, photorealistic, high detail.'
    ),
    (
        'banner_grand_ocean.png',
        'A powerful fleet of ships sailing across a vast ocean under a golden sunset sky. '
        'Multiple vessels in formation, dramatic clouds painted in gold and amber. '
        'Massive scale, showing dominance over the sea. '
        'Epic, grand atmosphere suggesting execution, growth, and mastery. '
        'Cinematic wide angle, photorealistic, high detail.'
    ),
]

# === Lesson images (800x500, generate at 16:9 then crop to 16:10) ===
LESSONS = [
    ('lesson_01.png',
     'A dramatic ocean scene with stormy seas and a compass, symbolizing the challenging EC marketplace. '
     'Dark clouds, waves, a lone ship navigating rough waters. Business metaphor. '
     'Professional photography style, photorealistic.'),
    ('lesson_02.png',
     'A business consultant having a warm conversation with a client across a table. '
     'Empathy and understanding. Modern office, warm lighting. Japanese business setting. Photorealistic.'),
    ('lesson_03.png',
     'A strategic war room with a large digital map showing competitor positions. '
     'Chess pieces on a board. Analytical atmosphere. Blue-toned professional lighting. Photorealistic.'),
    ('lesson_04.png',
     'A telescope pointing toward a clear blue ocean with an island in the distance. '
     'Discovery and opportunity. Golden light, hopeful mood. Photorealistic.'),
    ('lesson_05.png',
     'A bold flag waving on top of a ship mast against a clear sky. '
     'Brand identity, declaration, standing tall. Vibrant colors. Photorealistic.'),
    ('lesson_06.png',
     'An antique compass on a navigation chart with modern digital overlays. '
     'Strategy meets execution. Warm brass tones, professional. Photorealistic.'),
    ('lesson_07.png',
     'Precious gems being polished by skilled hands. Product refinement concept. '
     'Sparkling, luxurious atmosphere. Close-up, detailed. Photorealistic.'),
    ('lesson_08.png',
     'A modern digital navigation dashboard showing SEO and search routes. '
     'Data visualization with blue glowing lines on a dark background. Photorealistic.'),
    ('lesson_09.png',
     'A majestic large ship being built in a shipyard. Construction, building something substantial. '
     'Workers, scaffolding, dramatic scale. Photorealistic.'),
    ('lesson_10.png',
     'A sleek speedboat racing across crystal blue water. Speed, agility, dynamic motion blur. '
     'Splashing water, sunny day. Photorealistic.'),
    ('lesson_11.png',
     'A medieval armory with modern twist - swords replaced by advertising tools, screens, '
     'analytics dashboards. Strategic weapons for business. Photorealistic.'),
    ('lesson_12.png',
     'A vibrant marketplace on a harbor dock. Live commerce, face-to-face selling. '
     'Colorful, energetic atmosphere. People interacting, products displayed. Photorealistic.'),
    ('lesson_13.png',
     'An aerial view of a beautiful port town with shops, lights, and busy streets. '
     'Converting sales points into a thriving ecosystem. Warm evening glow. Photorealistic.'),
    ('lesson_14.png',
     'A ship fully loaded and ready to depart, crew standing on deck. Everything in order. '
     'Dawn breaking over the harbor. Anticipation and readiness. Photorealistic.'),
    ('lesson_15.png',
     'A captain studying navigation charts and planning routes on a large table. '
     'Detailed planning, maps, instruments. Warm lamp light. Photorealistic.'),
    ('lesson_16.png',
     'A captain looking through binoculars at the horizon from the bridge of a ship. '
     'Reading daily data, monitoring conditions. Clear sky, calm sea. Photorealistic.'),
    ('lesson_17.png',
     'A surfer riding a massive wave with perfect balance. Turning challenges into advantages. '
     'Power and skill. Ocean spray, dramatic lighting. Photorealistic.'),
    ('lesson_18.png',
     'A ship successfully navigating through an iceberg field at night. '
     'Avoiding danger. Caution and expertise. Cold blue moonlight. Photorealistic.'),
    ('lesson_19.png',
     'A fleet of ships sailing in formation with holographic digital overlays. '
     'Human captain commanding the fleet. Futuristic yet nautical. Photorealistic.'),
    ('lesson_20.png',
     'A merchant weighing gold coins on an antique scale with modern price tags nearby. '
     'Dynamic pricing concept. Rich warm tones, detailed textures. Photorealistic.'),
    ('lesson_21.png',
     'A ship hull being inspected and maintained in dry dock. Financial health check metaphor. '
     'Careful, methodical workers. Industrial setting. Photorealistic.'),
    ('lesson_22.png',
     'A strategist reviewing battle plans on a large table before engagement. '
     'Quality review, preparation wins. Confident posture, focused lighting. Photorealistic.'),
    ('lesson_23.png',
     'A large navigation chart being unrolled on a table revealing multiple routes and channels. '
     'Multi-channel expansion concept. Warm office lighting, maps, compasses. Photorealistic.'),
    ('lesson_24.png',
     'A hero standing at the bow of a ship, welcomed by a grateful crowd at the port. '
     'Trust and reputation. Warm golden light, celebration. Photorealistic.'),
    ('lesson_25.png',
     'An old leather-bound journal being written in by lantern light on a ship desk. '
     'Recording success and lessons. Ink pen, warm amber glow. Photorealistic.'),
    ('lesson_26.png',
     'A commanding view from a flagship overlooking a vast ocean with controlled sea lanes. '
     'Dominance and authority. Panoramic, powerful. Photorealistic.'),
    ('lesson_27.png',
     'A hero captain standing proudly on the deck of a ship at sunrise, crew cheering behind. '
     'The final achievement. Triumphant, golden morning light. Photorealistic.'),
]


def main():
    results = {'success': [], 'failed': []}

    print("=== Generating Banner Images (2 images, 1200x400) ===")
    for filename, prompt in BANNERS:
        ok = generate_and_save(filename, prompt, BANNER_SIZE, aspect_ratio='16:9')
        (results['success'] if ok else results['failed']).append(filename)
        time.sleep(2)  # Brief pause between requests

    print("\n=== Generating Lesson Images (27 images, 800x500) ===")
    for filename, prompt in LESSONS:
        ok = generate_and_save(filename, prompt, LESSON_SIZE, aspect_ratio='16:9')
        (results['success'] if ok else results['failed']).append(filename)
        time.sleep(2)  # Brief pause between requests

    print("\n=== RESULTS ===")
    print(f"Success: {len(results['success'])}/{len(BANNERS) + len(LESSONS)}")
    if results['failed']:
        print(f"Failed: {results['failed']}")

    # Verify all files
    print("\n=== FILE VERIFICATION ===")
    all_files = [b[0] for b in BANNERS] + [l[0] for l in LESSONS]
    for f in all_files:
        fp = OUTPUT_DIR / f
        if fp.exists():
            size_kb = fp.stat().st_size / 1024
            img = Image.open(fp)
            print(f"  OK  {f}: {img.size[0]}x{img.size[1]}, {size_kb:.0f}KB")
        else:
            print(f"  MISSING  {f}")

    return len(results['failed']) == 0


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
