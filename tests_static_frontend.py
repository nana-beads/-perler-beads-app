from pathlib import Path


def test_static_frontend_files_exist():
    root = Path('/Users/nana/perler-beads-app')
    assert (root / 'docs' / 'index.html').exists()
    assert (root / 'docs' / 'app.js').exists()
    assert (root / 'docs' / 'style.css').exists()


def test_static_frontend_mentions_github_pages_ready():
    html = (Path('/Users/nana/perler-beads-app') / 'docs' / 'index.html').read_text(encoding='utf-8')
    assert 'GitHub Pages' in html
    assert '浏览器本地处理' in html


def test_static_frontend_has_core_controls():
    html = (Path('/Users/nana/perler-beads-app') / 'docs' / 'index.html').read_text(encoding='utf-8')
    assert 'name="image"' in html
    assert 'name="gridWidth"' in html
    assert 'name="paletteMode"' in html
    assert 'name="maxColors"' in html


def test_static_frontend_has_generation_logic():
    js = (Path('/Users/nana/perler-beads-app') / 'docs' / 'app.js').read_text(encoding='utf-8')
    assert 'function generatePattern' in js
    assert 'function nearestColor' in js
    assert 'function downloadCanvas' in js
