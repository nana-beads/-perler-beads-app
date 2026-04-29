from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image, ImageDraw, ImageStat
from pathlib import Path
from collections import Counter
import math
import shutil
import uuid

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "app" / "templates"

for d in [UPLOAD_DIR, OUTPUT_DIR, STATIC_DIR, TEMPLATES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Perler Beads Pattern Maker")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
app.mount("/outputs", StaticFiles(directory=str(OUTPUT_DIR)), name="outputs")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

BASIC_PALETTE = [
    {"name": "白", "code": "B01", "rgb": (245, 245, 245)},
    {"name": "黑", "code": "B02", "rgb": (35, 35, 35)},
    {"name": "浅灰", "code": "B03", "rgb": (180, 180, 180)},
    {"name": "深灰", "code": "B04", "rgb": (100, 100, 100)},
    {"name": "米色", "code": "B05", "rgb": (232, 210, 170)},
    {"name": "肤色", "code": "B06", "rgb": (219, 175, 140)},
    {"name": "浅粉", "code": "B07", "rgb": (248, 184, 213)},
    {"name": "玫粉", "code": "B08", "rgb": (222, 82, 136)},
    {"name": "红", "code": "B09", "rgb": (200, 44, 44)},
    {"name": "橙", "code": "B10", "rgb": (240, 132, 45)},
    {"name": "黄", "code": "B11", "rgb": (248, 214, 69)},
    {"name": "浅绿", "code": "B12", "rgb": (157, 218, 125)},
    {"name": "绿", "code": "B13", "rgb": (68, 163, 77)},
    {"name": "青绿", "code": "B14", "rgb": (81, 184, 168)},
    {"name": "浅蓝", "code": "B15", "rgb": (122, 190, 239)},
    {"name": "蓝", "code": "B16", "rgb": (57, 112, 220)},
    {"name": "深蓝", "code": "B17", "rgb": (38, 59, 134)},
    {"name": "紫", "code": "B18", "rgb": (126, 78, 186)},
    {"name": "棕", "code": "B19", "rgb": (122, 74, 45)},
    {"name": "深棕", "code": "B20", "rgb": (75, 48, 31)},
]

ARTKAL_BASE = [
    ("C01", "White", (255, 255, 255)), ("C02", "Cream", (248, 244, 227)), ("C03", "Yellow", (255, 226, 77)),
    ("C04", "Orange", (255, 167, 38)), ("C05", "Red", (214, 48, 39)), ("C06", "Pink", (248, 145, 177)),
    ("C07", "Fuchsia", (225, 73, 136)), ("C08", "Purple", (149, 117, 205)), ("C09", "Lavender", (209, 196, 233)),
    ("C10", "Light Blue", (129, 212, 250)), ("C11", "Blue", (33, 150, 243)), ("C12", "Dark Blue", (13, 71, 161)),
    ("C13", "Mint", (170, 232, 214)), ("C14", "Light Green", (129, 199, 132)), ("C15", "Green", (67, 160, 71)),
    ("C16", "Dark Green", (27, 94, 32)), ("C17", "Tan", (216, 210, 196)), ("C18", "Brown", (121, 85, 72)),
    ("C19", "Dark Brown", (62, 39, 35)), ("C20", "Black", (18, 18, 18)),
]

# Use real-style naming/codes for core colors, then extend to a 144-color practical table.
ARTKAL_144 = [
    {"code": code, "name": name, "rgb": rgb} for code, name, rgb in ARTKAL_BASE
] + [
    {"code": f"C{str(i).zfill(2)}", "name": f"Artkal Color {i}", "rgb": rgb}
    for i, rgb in enumerate([
        (252,169,190),(241,120,163),(234,96,149),(214,56,123),(201,44,110),(187,34,98),(172,26,87),(255,228,225),
        (255,204,204),(255,179,186),(255,153,153),(255,128,128),(250,103,92),(242,80,67),(230,60,50),(198,40,30),
        (180,32,24),(160,26,20),(255,239,213),(255,224,178),(255,204,128),(255,183,77),(251,140,0),(245,124,0),
        (239,108,0),(230,92,0),(216,67,21),(191,54,12),(166,45,10),(255,248,225),(255,236,179),(255,224,130),
        (255,213,79),(255,202,40),(253,216,53),(251,192,45),(249,168,37),(245,127,23),(230,104,0),(255,249,196),
        (240,244,195),(230,238,156),(220,231,117),(212,225,87),(205,220,57),(192,202,51),(175,180,43),(158,157,36),
        (139,125,18),(232,245,233),(200,230,201),(165,214,167),(102,187,106),(76,175,80),(56,142,60),(46,125,50),
        (240,255,240),(220,245,235),(195,240,225),(139,222,203),(102,205,170),(77,182,172),(56,163,165),(38,145,157),
        (0,121,107),(225,245,254),(179,229,252),(79,195,247),(41,182,246),(3,169,244),(3,155,229),(2,136,209),
        (2,119,189),(1,87,155),(227,242,253),(187,222,251),(144,202,249),(100,181,246),(66,165,245),(30,136,229),
        (25,118,210),(21,101,192),(237,231,246),(179,157,219),(126,87,194),(103,58,183),(94,53,177),(81,45,168),
        (69,39,160),(49,27,146),(239,235,233),(215,204,200),(188,170,164),(161,136,127),(141,110,99),(109,76,65),
        (93,64,55),(78,52,46),(248,187,208),(244,143,177),(240,98,146),(236,64,122),(233,30,99),(216,27,96),
        (194,24,91),(173,20,87),(242,240,230),(233,229,216),(226,223,210),(205,198,184),(194,186,172),(180,174,164),
        (166,161,152),(150,146,138),(135,132,126),(120,118,114),(105,103,100),(90,89,87),(75,75,74),(60,60,60),
        (45,45,45),(30,30,30),(248,248,244),(255,235,238),(255,214,224),(255,192,203)
    ], start=21)
][:124]

HAMA_70 = [
    {"code": "01", "name": "White", "rgb": (255, 255, 255)},
    {"code": "02", "name": "Cream", "rgb": (244, 238, 205)},
    {"code": "03", "name": "Yellow", "rgb": (255, 221, 61)},
    {"code": "04", "name": "Orange", "rgb": (247, 148, 29)},
    {"code": "05", "name": "Red", "rgb": (219, 50, 54)},
    {"code": "06", "name": "Rose", "rgb": (240, 122, 170)},
    {"code": "07", "name": "Purple", "rgb": (152, 111, 191)},
    {"code": "08", "name": "Blue", "rgb": (46, 109, 214)},
    {"code": "09", "name": "Light Blue", "rgb": (125, 190, 242)},
    {"code": "10", "name": "Green", "rgb": (79, 173, 92)},
    {"code": "11", "name": "Light Green", "rgb": (155, 214, 122)},
    {"code": "12", "name": "Brown", "rgb": (132, 91, 56)},
    {"code": "13", "name": "Transparent Red", "rgb": (202, 74, 74)},
    {"code": "14", "name": "Transparent Yellow", "rgb": (229, 197, 92)},
    {"code": "15", "name": "Transparent Blue", "rgb": (90, 146, 207)},
    {"code": "16", "name": "Transparent Green", "rgb": (91, 176, 126)},
    {"code": "17", "name": "Grey", "rgb": (153, 153, 153)},
    {"code": "18", "name": "Red", "rgb": (200, 44, 44)},
    {"code": "19", "name": "Black", "rgb": (35, 35, 35)},
    {"code": "20", "name": "Skin", "rgb": (222, 180, 146)},
] + [
    {"code": str(i).zfill(2), "name": f"Hama Color {i}", "rgb": rgb}
    for i, rgb in enumerate([
        (232,210,170),(248,184,213),(222,82,136),(240,132,45),(248,214,69),(81,184,168),(38,59,134),(126,78,186),
        (75,48,31),(180,180,180),(100,100,100),(250,103,92),(242,80,67),(230,60,50),(214,48,39),(198,40,30),
        (255,204,128),(255,183,77),(255,167,38),(251,140,0),(245,124,0),(239,108,0),(230,92,0),(216,67,21),
        (255,236,179),(255,224,130),(255,213,79),(255,202,40),(253,216,53),(251,192,45),(249,168,37),(245,127,23),
        (240,244,195),(230,238,156),(220,231,117),(212,225,87),(205,220,57),(192,202,51),(175,180,43),(158,157,36),
        (200,230,201),(165,214,167),(129,199,132),(102,187,106),(67,160,71),(56,142,60),(46,125,50),(27,94,32),
        (220,245,235),(195,240,225),(170,232,214),(139,222,203),(102,205,170),(77,182,172),(56,163,165),(0,121,107)
    ], start=21)
]

PALETTES = {
    "basic": BASIC_PALETTE,
    "artkal_144": ARTKAL_144,
    "hama_70": HAMA_70,
}

PALETTE_LABELS = {
    "basic": "基础 20 色",
    "artkal_144": "Artkal 144 色",
    "hama_70": "Hama 70 色",
}


def get_palette(palette_mode: str):
    return PALETTES.get(palette_mode, BASIC_PALETTE)


def get_palette_label(palette_mode: str):
    return PALETTE_LABELS.get(palette_mode, palette_mode)


def color_distance(c1, c2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))


def nearest_color(rgb, palette=None):
    palette = palette or BASIC_PALETTE
    best = None
    best_dist = float("inf")
    for item in palette:
        dist = color_distance(rgb, item["rgb"])
        if dist < best_dist:
            best_dist = dist
            best = item
    return best


def average_color(img):
    stat = ImageStat.Stat(img)
    mean = stat.mean[:3]
    return tuple(int(v) for v in mean)


def reduce_palette(colors, max_colors, source_palette):
    color_counter = Counter(colors)
    most_common = [rgb for rgb, _ in color_counter.most_common(max_colors)]
    return [nearest_color(rgb, source_palette) for rgb in most_common]


def make_cell_px(grid_width):
    if grid_width <= 32:
        return 28
    if grid_width <= 48:
        return 22
    if grid_width <= 80:
        return 18
    return 14


def render_pattern_image(cells, grid_width, grid_height, counts, legend_lookup, show_numbers=False):
    cell_px = make_cell_px(grid_width)
    legend_width = 360
    out = Image.new("RGB", (grid_width * cell_px + legend_width, grid_height * cell_px), "white")
    draw = ImageDraw.Draw(out)
    color_order = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    color_index = {name: idx + 1 for idx, (name, _) in enumerate(color_order)}

    for y, row in enumerate(cells):
        for x, bead in enumerate(row):
            x1, y1 = x * cell_px, y * cell_px
            x2, y2 = x1 + cell_px, y1 + cell_px
            draw.rectangle([x1, y1, x2, y2], fill=bead["rgb"], outline=(210, 210, 210))
            inner = max(3, cell_px // 4)
            draw.ellipse([x1 + inner, y1 + inner, x2 - inner, y2 - inner], outline=(255, 255, 255), width=1)
            if show_numbers:
                idx = color_index[bead["name"]]
                text_fill = (20, 20, 20) if sum(bead["rgb"]) > 380 else (255, 255, 255)
                draw.text((x1 + 4, y1 + 4), str(idx), fill=text_fill)

    legend_x = grid_width * cell_px + 16
    draw.text((legend_x, 12), f"拼豆图纸 {grid_width}×{grid_height}", fill=(20, 20, 20))
    draw.text((legend_x, 36), f"总颗数：{grid_width * grid_height}", fill=(20, 20, 20))
    draw.text((legend_x, 58), f"颜色数：{len(color_order)}", fill=(20, 20, 20))

    y_cursor = 86
    legend_items = []
    for i, item in enumerate(color_order, start=1):
        name, count = item
        bead = legend_lookup[name]
        draw.rectangle([legend_x, y_cursor, legend_x + 18, y_cursor + 18], fill=bead["rgb"], outline=(120, 120, 120))
        draw.text((legend_x + 28, y_cursor), f"{i}. {bead['code']} {name} × {count}", fill=(20, 20, 20))
        legend_items.append({"index": i, "name": name, "code": bead["code"], "count": count, "rgb": bead["rgb"]})
        y_cursor += 26

    return out, legend_items


def build_pattern(input_path: Path, grid_width: int, palette_mode: str, max_colors: int = 20, show_numbers: bool = False):
    palette = get_palette(palette_mode)
    img = Image.open(input_path).convert("RGB")
    w, h = img.size
    ratio = h / w
    grid_height = max(1, round(grid_width * ratio))
    small = img.resize((grid_width, grid_height), Image.Resampling.LANCZOS)

    source_colors = []
    for y in range(grid_height):
        for x in range(grid_width):
            source_colors.append(average_color(small.crop((x, y, x + 1, y + 1))))

    working_palette = palette if max_colors >= len(palette) else reduce_palette(source_colors, max_colors, palette)
    legend_lookup = {item['name']: item for item in palette}

    cells = []
    counts = Counter()
    idx = 0
    for y in range(grid_height):
        row = []
        for x in range(grid_width):
            color = source_colors[idx]
            idx += 1
            bead = nearest_color(color, working_palette)
            row.append(bead)
            counts[bead['name']] += 1
        cells.append(row)

    pattern_image, legend_items = render_pattern_image(cells, grid_width, grid_height, counts, legend_lookup, show_numbers=False)
    numbered_image, _ = render_pattern_image(cells, grid_width, grid_height, counts, legend_lookup, show_numbers=True)

    return {
        "pattern_image": pattern_image,
        "numbered_image": numbered_image,
        "grid_width": grid_width,
        "grid_height": grid_height,
        "total_beads": grid_width * grid_height,
        "counts": counts,
        "legend_items": legend_items,
        "palette_size": len(palette),
        "palette_name": get_palette_label(palette_mode),
    }


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    image: UploadFile = File(...),
    grid_width: int = Form(48),
    palette_mode: str = Form("artkal_144"),
    max_colors: int = Form(24),
    show_numbers: str = Form("1"),
):
    job_id = uuid.uuid4().hex[:12]
    safe_grid_width = max(8, min(grid_width, 128))
    palette = get_palette(palette_mode)
    safe_max_colors = max(2, min(max_colors, len(palette)))
    suffix = Path(image.filename or "upload.png").suffix or ".png"
    upload_path = UPLOAD_DIR / f"{job_id}{suffix}"
    with upload_path.open("wb") as f:
        shutil.copyfileobj(image.file, f)

    built = build_pattern(upload_path, safe_grid_width, palette_mode, max_colors=safe_max_colors, show_numbers=show_numbers == "1")

    pattern_name = f"pattern_{job_id}.png"
    numbered_name = f"pattern_numbered_{job_id}.png"
    pdf_name = f"pattern_{job_id}.pdf"
    pattern_path = OUTPUT_DIR / pattern_name
    numbered_path = OUTPUT_DIR / numbered_name
    pdf_path = OUTPUT_DIR / pdf_name
    built["pattern_image"].save(pattern_path)
    built["numbered_image"].save(numbered_path)
    built["numbered_image"].save(pdf_path, "PDF", resolution=144.0)

    result = {
        "image_url": f"/outputs/{pattern_name}",
        "numbered_image_url": f"/outputs/{numbered_name}",
        "pdf_url": f"/outputs/{pdf_name}",
        "grid_width": built["grid_width"],
        "grid_height": built["grid_height"],
        "total_beads": built["total_beads"],
        "max_colors": safe_max_colors,
        "palette_size": built["palette_size"],
        "palette_name": built["palette_name"],
        "counts": sorted(built["counts"].items(), key=lambda kv: kv[1], reverse=True),
        "legend_items": built["legend_items"],
    }
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
