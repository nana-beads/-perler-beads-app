const BASIC_PALETTE = [
  { name: '白', code: 'B01', rgb: [245, 245, 245] },
  { name: '黑', code: 'B02', rgb: [35, 35, 35] },
  { name: '浅灰', code: 'B03', rgb: [180, 180, 180] },
  { name: '深灰', code: 'B04', rgb: [100, 100, 100] },
  { name: '米色', code: 'B05', rgb: [232, 210, 170] },
  { name: '肤色', code: 'B06', rgb: [219, 175, 140] },
  { name: '浅粉', code: 'B07', rgb: [248, 184, 213] },
  { name: '玫粉', code: 'B08', rgb: [222, 82, 136] },
  { name: '红', code: 'B09', rgb: [200, 44, 44] },
  { name: '橙', code: 'B10', rgb: [240, 132, 45] },
  { name: '黄', code: 'B11', rgb: [248, 214, 69] },
  { name: '浅绿', code: 'B12', rgb: [157, 218, 125] },
  { name: '绿', code: 'B13', rgb: [68, 163, 77] },
  { name: '青绿', code: 'B14', rgb: [81, 184, 168] },
  { name: '浅蓝', code: 'B15', rgb: [122, 190, 239] },
  { name: '蓝', code: 'B16', rgb: [57, 112, 220] },
  { name: '深蓝', code: 'B17', rgb: [38, 59, 134] },
  { name: '紫', code: 'B18', rgb: [126, 78, 186] },
  { name: '棕', code: 'B19', rgb: [122, 74, 45] },
  { name: '深棕', code: 'B20', rgb: [75, 48, 31] },
];

const ARTKAL_BASE = [
  ['C01', 'White', [255, 255, 255]], ['C02', 'Cream', [248, 244, 227]], ['C03', 'Yellow', [255, 226, 77]],
  ['C04', 'Orange', [255, 167, 38]], ['C05', 'Red', [214, 48, 39]], ['C06', 'Pink', [248, 145, 177]],
  ['C07', 'Fuchsia', [225, 73, 136]], ['C08', 'Purple', [149, 117, 205]], ['C09', 'Lavender', [209, 196, 233]],
  ['C10', 'Light Blue', [129, 212, 250]], ['C11', 'Blue', [33, 150, 243]], ['C12', 'Dark Blue', [13, 71, 161]],
  ['C13', 'Mint', [170, 232, 214]], ['C14', 'Light Green', [129, 199, 132]], ['C15', 'Green', [67, 160, 71]],
  ['C16', 'Dark Green', [27, 94, 32]], ['C17', 'Tan', [216, 210, 196]], ['C18', 'Brown', [121, 85, 72]],
  ['C19', 'Dark Brown', [62, 39, 35]], ['C20', 'Black', [18, 18, 18]],
];

const ARTKAL_EXTRA_RGBS = [
  [252,169,190],[241,120,163],[234,96,149],[214,56,123],[201,44,110],[187,34,98],[172,26,87],[255,228,225],
  [255,204,204],[255,179,186],[255,153,153],[255,128,128],[250,103,92],[242,80,67],[230,60,50],[198,40,30],
  [180,32,24],[160,26,20],[255,239,213],[255,224,178],[255,204,128],[255,183,77],[251,140,0],[245,124,0],
  [239,108,0],[230,92,0],[216,67,21],[191,54,12],[166,45,10],[255,248,225],[255,236,179],[255,224,130],
  [255,213,79],[255,202,40],[253,216,53],[251,192,45],[249,168,37],[245,127,23],[230,104,0],[255,249,196],
  [240,244,195],[230,238,156],[220,231,117],[212,225,87],[205,220,57],[192,202,51],[175,180,43],[158,157,36],
  [139,125,18],[232,245,233],[200,230,201],[165,214,167],[102,187,106],[76,175,80],[56,142,60],[46,125,50],
  [240,255,240],[220,245,235],[195,240,225],[139,222,203],[102,205,170],[77,182,172],[56,163,165],[38,145,157],
  [0,121,107],[225,245,254],[179,229,252],[79,195,247],[41,182,246],[3,169,244],[3,155,229],[2,136,209],
  [2,119,189],[1,87,155],[227,242,253],[187,222,251],[144,202,249],[100,181,246],[66,165,245],[30,136,229],
  [25,118,210],[21,101,192],[237,231,246],[179,157,219],[126,87,194],[103,58,183],[94,53,177],[81,45,168],
  [69,39,160],[49,27,146],[239,235,233],[215,204,200],[188,170,164],[161,136,127],[141,110,99],[109,76,65],
  [93,64,55],[78,52,46],[248,187,208],[244,143,177],[240,98,146],[236,64,122],[233,30,99],[216,27,96],
  [194,24,91],[173,20,87],[242,240,230],[233,229,216],[226,223,210],[205,198,184],[194,186,172],[180,174,164],
  [166,161,152],[150,146,138],[135,132,126],[120,118,114],[105,103,100],[90,89,87],[75,75,74],[60,60,60],
  [45,45,45],[30,30,30],[248,248,244],[255,235,238],[255,214,224],[255,192,203]
];

const ARTKAL_144 = [
  ...ARTKAL_BASE.map(([code, name, rgb]) => ({ code, name, rgb })),
  ...ARTKAL_EXTRA_RGBS.map((rgb, index) => {
    const code = `C${String(index + 21).padStart(2, '0')}`;
    return { code, name: `Artkal Color ${index + 21}`, rgb };
  }).slice(0, 124)
];

const HAMA_BASE = [
  ['01', 'White', [255, 255, 255]], ['02', 'Cream', [244, 238, 205]], ['03', 'Yellow', [255, 221, 61]],
  ['04', 'Orange', [247, 148, 29]], ['05', 'Red', [219, 50, 54]], ['06', 'Rose', [240, 122, 170]],
  ['07', 'Purple', [152, 111, 191]], ['08', 'Blue', [46, 109, 214]], ['09', 'Light Blue', [125, 190, 242]],
  ['10', 'Green', [79, 173, 92]], ['11', 'Light Green', [155, 214, 122]], ['12', 'Brown', [132, 91, 56]],
  ['13', 'Transparent Red', [202, 74, 74]], ['14', 'Transparent Yellow', [229, 197, 92]], ['15', 'Transparent Blue', [90, 146, 207]],
  ['16', 'Transparent Green', [91, 176, 126]], ['17', 'Grey', [153, 153, 153]], ['18', 'Red', [200, 44, 44]],
  ['19', 'Black', [35, 35, 35]], ['20', 'Skin', [222, 180, 146]],
];

const HAMA_EXTRA_RGBS = [
  [232,210,170],[248,184,213],[222,82,136],[240,132,45],[248,214,69],[81,184,168],[38,59,134],[126,78,186],
  [75,48,31],[180,180,180],[100,100,100],[250,103,92],[242,80,67],[230,60,50],[214,48,39],[198,40,30],
  [255,204,128],[255,183,77],[255,167,38],[251,140,0],[245,124,0],[239,108,0],[230,92,0],[216,67,21],
  [255,236,179],[255,224,130],[255,213,79],[255,202,40],[253,216,53],[251,192,45],[249,168,37],[245,127,23],
  [240,244,195],[230,238,156],[220,231,117],[212,225,87],[205,220,57],[192,202,51],[175,180,43],[158,157,36],
  [200,230,201],[165,214,167],[129,199,132],[102,187,106],[67,160,71],[56,142,60],[46,125,50],[27,94,32],
  [220,245,235],[195,240,225],[170,232,214],[139,222,203],[102,205,170],[77,182,172],[56,163,165],[0,121,107]
];

const HAMA_70 = [
  ...HAMA_BASE.map(([code, name, rgb]) => ({ code, name, rgb })),
  ...HAMA_EXTRA_RGBS.map((rgb, index) => ({ code: String(index + 21).padStart(2, '0'), name: `Hama Color ${index + 21}`, rgb }))
];

const PALETTES = {
  basic: BASIC_PALETTE,
  artkal_144: ARTKAL_144,
  hama_70: HAMA_70,
};

const PALETTE_LABELS = {
  basic: '基础 20 色',
  artkal_144: 'Artkal 144 色',
  hama_70: 'Hama 70 色',
};

const imageInput = document.getElementById('imageInput');
const gridWidthInput = document.getElementById('gridWidth');
const maxColorsInput = document.getElementById('maxColors');
const paletteModeInput = document.getElementById('paletteMode');
const generateBtn = document.getElementById('generateBtn');
const downloadColorBtn = document.getElementById('downloadColorBtn');
const downloadNumberedBtn = document.getElementById('downloadNumberedBtn');
const colorCanvas = document.getElementById('colorCanvas');
const numberedCanvas = document.getElementById('numberedCanvas');
const statusBox = document.getElementById('status');
const metaBox = document.getElementById('meta');
const legendBody = document.getElementById('legendBody');

let latestResult = null;

function colorDistance(a, b) {
  const dr = a[0] - b[0];
  const dg = a[1] - b[1];
  const db = a[2] - b[2];
  return Math.sqrt(dr * dr + dg * dg + db * db);
}

function nearestColor(rgb, palette) {
  let best = palette[0];
  let bestDist = Infinity;
  for (const item of palette) {
    const dist = colorDistance(rgb, item.rgb);
    if (dist < bestDist) {
      best = item;
      bestDist = dist;
    }
  }
  return best;
}

function reducePalette(sourceColors, maxColors, palette) {
  const counts = new Map();
  for (const color of sourceColors) {
    const key = color.join(',');
    counts.set(key, (counts.get(key) || 0) + 1);
  }
  const top = [...counts.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, maxColors)
    .map(([key]) => key.split(',').map(Number));
  return top.map((rgb) => nearestColor(rgb, palette));
}

function makeCellPx(gridWidth) {
  if (gridWidth <= 32) return 28;
  if (gridWidth <= 48) return 22;
  if (gridWidth <= 80) return 18;
  return 14;
}

function getTextColor(rgb) {
  const sum = rgb[0] + rgb[1] + rgb[2];
  return sum > 380 ? '#111827' : '#ffffff';
}

function drawCell(ctx, x, y, cellPx, bead) {
  ctx.fillStyle = `rgb(${bead.rgb.join(',')})`;
  ctx.fillRect(x, y, cellPx, cellPx);
  ctx.strokeStyle = '#d1d5db';
  ctx.strokeRect(x, y, cellPx, cellPx);
  ctx.beginPath();
  const inner = Math.max(3, Math.floor(cellPx / 4));
  ctx.strokeStyle = 'rgba(255,255,255,.7)';
  ctx.arc(x + cellPx / 2, y + cellPx / 2, Math.max(2, cellPx / 2 - inner), 0, Math.PI * 2);
  ctx.stroke();
}

function renderPattern(ctx, result, showNumbers) {
  const { cells, gridWidth, gridHeight, legendItems } = result;
  const cellPx = makeCellPx(gridWidth);
  ctx.canvas.width = gridWidth * cellPx;
  ctx.canvas.height = gridHeight * cellPx;
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);

  const numberMap = new Map(legendItems.map((item) => [item.name, item.index]));

  for (let y = 0; y < gridHeight; y += 1) {
    for (let x = 0; x < gridWidth; x += 1) {
      const bead = cells[y][x];
      const px = x * cellPx;
      const py = y * cellPx;
      drawCell(ctx, px, py, cellPx, bead);
      if (showNumbers) {
        ctx.fillStyle = getTextColor(bead.rgb);
        ctx.font = `${Math.max(10, Math.floor(cellPx * 0.45))}px sans-serif`;
        ctx.fillText(String(numberMap.get(bead.name) || ''), px + 4, py + Math.max(12, Math.floor(cellPx * 0.62)));
      }
    }
  }
}

function renderLegend(legendItems) {
  legendBody.innerHTML = '';
  if (!legendItems.length) {
    legendBody.innerHTML = '<tr><td colspan="4">生成后在这里显示</td></tr>';
    return;
  }
  legendItems.forEach((item) => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${item.index}</td><td>${item.code}</td><td>${item.name}</td><td>${item.count}</td>`;
    legendBody.appendChild(tr);
  });
}

function downloadCanvas(canvas, filename) {
  const link = document.createElement('a');
  link.href = canvas.toDataURL('image/png');
  link.download = filename;
  link.click();
}

function loadImage(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const img = new Image();
      img.onload = () => resolve(img);
      img.onerror = reject;
      img.src = reader.result;
    };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

function samplePixels(image, gridWidth, gridHeight) {
  const canvas = document.createElement('canvas');
  canvas.width = gridWidth;
  canvas.height = gridHeight;
  const ctx = canvas.getContext('2d', { willReadFrequently: true });
  ctx.drawImage(image, 0, 0, gridWidth, gridHeight);
  const data = ctx.getImageData(0, 0, gridWidth, gridHeight).data;
  const pixels = [];
  for (let i = 0; i < data.length; i += 4) {
    pixels.push([data[i], data[i + 1], data[i + 2]]);
  }
  return pixels;
}

function generatePattern(image, gridWidth, paletteMode, maxColors) {
  const palette = PALETTES[paletteMode] || BASIC_PALETTE;
  const gridHeight = Math.max(1, Math.round(gridWidth * (image.height / image.width)));
  const sourceColors = samplePixels(image, gridWidth, gridHeight);
  const workingPalette = maxColors >= palette.length ? palette : reducePalette(sourceColors, maxColors, palette);
  const cells = [];
  const counts = new Map();
  let idx = 0;

  for (let y = 0; y < gridHeight; y += 1) {
    const row = [];
    for (let x = 0; x < gridWidth; x += 1) {
      const bead = nearestColor(sourceColors[idx], workingPalette);
      row.push(bead);
      counts.set(bead.name, (counts.get(bead.name) || 0) + 1);
      idx += 1;
    }
    cells.push(row);
  }

  const legendLookup = new Map(palette.map((item) => [item.name, item]));
  const legendItems = [...counts.entries()]
    .sort((a, b) => b[1] - a[1])
    .map(([name, count], index) => {
      const bead = legendLookup.get(name);
      return { index: index + 1, name, code: bead.code, rgb: bead.rgb, count };
    });

  return {
    cells,
    gridWidth,
    gridHeight,
    totalBeads: gridWidth * gridHeight,
    legendItems,
    paletteName: PALETTE_LABELS[paletteMode] || paletteMode,
    paletteSize: palette.length,
  };
}

async function handleGenerate() {
  const file = imageInput.files?.[0];
  if (!file) {
    statusBox.textContent = '请先上传图片。';
    return;
  }

  generateBtn.disabled = true;
  statusBox.textContent = '正在生成，请稍候…';

  try {
    const image = await loadImage(file);
    const gridWidth = Math.max(8, Math.min(128, Number(gridWidthInput.value) || 48));
    const paletteMode = paletteModeInput.value;
    const paletteSize = (PALETTES[paletteMode] || BASIC_PALETTE).length;
    const maxColors = Math.max(2, Math.min(paletteSize, Number(maxColorsInput.value) || 24));
    const result = generatePattern(image, gridWidth, paletteMode, maxColors);

    renderPattern(colorCanvas.getContext('2d'), result, false);
    renderPattern(numberedCanvas.getContext('2d'), result, true);
    renderLegend(result.legendItems);

    metaBox.textContent = `色卡：${result.paletteName}（${result.paletteSize} 色）｜尺寸：${result.gridWidth} × ${result.gridHeight} ｜ 总颗数：${result.totalBeads} ｜ 实际颜色数：${result.legendItems.length}/${maxColors}`;
    statusBox.textContent = '生成完成，可以预览并下载 PNG。';

    latestResult = result;
    downloadColorBtn.disabled = false;
    downloadNumberedBtn.disabled = false;
  } catch (error) {
    console.error(error);
    statusBox.textContent = '生成失败，请换一张图片重试。';
  } finally {
    generateBtn.disabled = false;
  }
}

generateBtn.addEventListener('click', handleGenerate);
downloadColorBtn.addEventListener('click', () => {
  if (!latestResult) return;
  downloadCanvas(colorCanvas, 'perler-pattern-color.png');
});
downloadNumberedBtn.addEventListener('click', () => {
  if (!latestResult) return;
  downloadCanvas(numberedCanvas, 'perler-pattern-numbered.png');
});
