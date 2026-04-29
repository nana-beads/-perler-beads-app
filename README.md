# 拼豆图纸生成器

一个可公开部署的网页版应用：上传图片，自动生成拼豆参考图纸 PNG / PDF，并统计各颜色颗数。

## 功能
- 上传任意图片
- 按指定横向颗数缩放为拼豆网格
- 支持基础 20 色、Artkal 144 色、Hama 70 色色卡
- 自动映射到拼豆色板并统计颜色数量
- 输出彩色图纸、编号图纸、PDF
- 页面中直接预览并下载
- 已整理为可部署到 **Render / Railway** 的公开网页版

## 本地运行

```bash
cd /Users/nana/perler-beads-app
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

浏览器打开：

```text
http://127.0.0.1:8000
```

## 生产部署

### 方式一：Render
1. 把项目上传到 GitHub
2. 在 Render 新建 **Web Service**
3. 连接你的 GitHub 仓库
4. 配置：
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
5. 部署完成后即可获得公开链接

### 方式二：Railway
1. 把项目上传到 GitHub
2. 在 Railway 新建项目并导入仓库
3. Railway 会自动读取 `Procfile`
4. 部署完成后即可获得公开链接

## 部署文件
- `requirements.txt`
- `Procfile`
- `.gitignore`

## 说明
- 当前版本适合先快速公开分享给别人试用
- 上传图片与生成结果默认保存在本地 `uploads/` 与 `outputs/`
- 如果正式商用，建议后续增加：
  - 自动清理历史文件
  - 用户任务队列
  - 图片大小限制
  - 分板切片
  - CDN / 对象存储
  - 登录与配额控制

## 后续可继续增强
- 按板子尺寸自动切片
- 更完整的 Artkal / Hama 官方色号映射
- 公开分享页面优化
- 微信小程序版
