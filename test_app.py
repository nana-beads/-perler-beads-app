from PIL import Image, ImageDraw
from pathlib import Path
from app.main import build_pattern

base = Path('/Users/nana/perler-beads-app')
src = base / 'test_input.png'
img = Image.new('RGB', (16, 16), 'white')
d = ImageDraw.Draw(img)
d.rectangle([0,0,7,7], fill=(255,0,0))
d.rectangle([8,0,15,7], fill=(0,255,0))
d.rectangle([0,8,7,15], fill=(0,0,255))
d.rectangle([8,8,15,15], fill=(255,255,0))
img.save(src)
result = build_pattern(src, 16, 'basic', max_colors=12, show_numbers=True)
result['pattern_image'].save(base / 'outputs' / 'test_pattern.png')
result['numbered_image'].save(base / 'outputs' / 'test_pattern_numbered.png')
print(result['grid_height'])
print(result['total_beads'])
print(sorted(result['counts'].items(), key=lambda kv: kv[1], reverse=True))
