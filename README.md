# 拼豆图纸生成器

现在这个项目同时包含两套版本：

1. **本地 FastAPI 版**：适合继续做后端增强功能
2. **免费纯前端静态版**：放在 `docs/`，适合部署到 **GitHub Pages**，不需要服务器、不需要绑卡

## 免费公开分享版（推荐）

纯前端静态版位于：

- `docs/index.html`
- `docs/style.css`
- `docs/app.js`

特点：
- 浏览器本地处理图片
- 不上传服务器
- 不需要 Render / Railway / 绑卡
- 可直接部署到 GitHub Pages 免费分享

### 本地预览静态版
直接双击打开：

```text
docs/index.html
```

或者用本地静态服务：

```bash
cd /Users/nana/perler-beads-app
python -m http.server 8080
```

然后浏览器打开：

```text
http://127.0.0.1:8080/docs/
```

## GitHub Pages 发布步骤

### 1. 打开你的 GitHub 仓库
仓库地址：

```text
https://github.com/nana-beads/-perler-beads-app
```

### 2. 进入仓库设置
点击：
- `Settings`
- 左侧点击 `Pages`

### 3. 设置发布来源
在 `Build and deployment` 里设置：
- **Source**: `Deploy from a branch`
- **Branch**: `main`
- **Folder**: `/docs`

然后点击 **Save**。

### 4. 等待 GitHub Pages 发布
等几十秒到几分钟后，GitHub 会给你一个公开网址。
通常会类似：

```text
https://nana-beads.github.io/-perler-beads-app/
```

## 当前纯前端版支持
- 上传图片
- 设置横向颗数
- 设置最大颜色数
- 选择基础 20 色 / Artkal 144 色 / Hama 70 色
- 浏览器本地生成彩色拼豆图
- 浏览器本地生成编号拼豆图
- 下载彩色图 PNG
- 下载编号图 PNG
- 颜色统计表

## 当前纯前端版暂未包含
- PDF 导出
- 按板子自动切片
- 服务端存储
- 多用户任务队列

这些后续还可以继续加。

## 本地 FastAPI 版
如果你还要继续开发后端版：

```bash
cd /Users/nana/perler-beads-app
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

浏览器打开：

```text
http://127.0.0.1:8000
```
