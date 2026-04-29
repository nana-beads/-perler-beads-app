from pathlib import Path
from PIL import Image, ImageDraw
from app.main import app, build_pattern, get_palette, PALETTES
from fastapi.testclient import TestClient


def create_quadrant_image(path: Path):
    img = Image.new('RGB', (16, 16), 'white')
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 7, 7], fill=(255, 0, 0))
    d.rectangle([8, 0, 15, 7], fill=(0, 255, 0))
    d.rectangle([0, 8, 7, 15], fill=(0, 0, 255))
    d.rectangle([8, 8, 15, 15], fill=(255, 255, 0))
    img.save(path)


def test_artkal_144_palette_has_expected_size_and_real_codes():
    palette = get_palette('artkal_144')
    assert len(palette) == 144
    assert len(PALETTES['artkal_144']) == 144
    assert palette[0]['code'] == 'C01'
    assert palette[0]['name'] == 'White'
    assert any(item['code'] == 'C02' and item['name'] == 'Cream' for item in palette)


def test_hama_palette_has_real_codes():
    palette = get_palette('hama_70')
    assert len(palette) >= 60
    assert any(item['code'] == '01' and item['name'] == 'White' for item in palette)
    assert any(item['code'] == '18' and item['name'] == 'Red' for item in palette)


def test_build_pattern_counts_quadrants(tmp_path: Path):
    src = tmp_path / 'input.png'
    create_quadrant_image(src)
    result = build_pattern(src, 16, 'basic', max_colors=20, show_numbers=False)
    counts = result['counts']
    assert result['grid_height'] == 16
    assert result['total_beads'] == 256
    assert counts['红'] == 64
    assert counts['绿'] == 64
    assert counts['蓝'] == 64
    assert counts['黄'] == 64


def test_build_pattern_can_limit_colors(tmp_path: Path):
    src = tmp_path / 'input.png'
    create_quadrant_image(src)
    result = build_pattern(src, 16, 'artkal_144', max_colors=2, show_numbers=False)
    assert len(result['counts']) <= 2


def test_build_pattern_returns_numbered_and_color_images(tmp_path: Path):
    src = tmp_path / 'input.png'
    create_quadrant_image(src)
    result = build_pattern(src, 16, 'artkal_144', max_colors=20, show_numbers=True)
    assert result['pattern_image'].mode == 'RGB'
    assert result['numbered_image'].mode == 'RGB'
    assert result['legend_items']


def test_home_page_mentions_public_sharing_ready_text():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    html = response.text
    assert '公开网页版' in html
    assert '可部署到 Render / Railway' in html
