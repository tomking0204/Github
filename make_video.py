# make_video.py —— 用 Python 做一支 3 秒的小影片
# 需要先安裝：pip install pillow imageio imageio-ffmpeg numpy

from PIL import Image, ImageDraw   # Pillow：用來「畫」每一張圖
import imageio                      # imageio：把很多張圖接成影片
import numpy as np                  # numpy：把圖轉成數字陣列

# ===== 1. 基本設定 =====
WIDTH, HEIGHT = 640, 480   # 影片寬高（像素，最好是 16 的倍數）
FPS = 30                   # 每秒幾張圖（幀）
SECONDS = 3                # 影片長度
TOTAL_FRAMES = FPS * SECONDS   # 總共要畫幾張 = 90 張

# ===== 2. 開一個影片檔準備寫入 =====
writer = imageio.get_writer("my_video.mp4", fps=FPS)

# ===== 3. 用迴圈一張一張畫 =====
for i in range(TOTAL_FRAMES):
    progress = i / (TOTAL_FRAMES - 1)   # 從 0 慢慢變到 1，代表影片進度

    # 3-1 開一張新的空白圖（深藍色背景）
    img = Image.new("RGB", (WIDTH, HEIGHT), (20, 30, 60))
    draw = ImageDraw.Draw(img)

    # 3-2 算出圓球這一幀的位置：從左邊移動到右邊
    radius = 40
    x = radius + progress * (WIDTH - 2 * radius)
    y = HEIGHT // 2

    # 3-3 顏色也跟著進度變：從紅色慢慢變成綠色
    color = (int(255 * (1 - progress)), int(255 * progress), 120)

    # 3-4 畫出圓球
    draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)

    # 3-5 在左上角寫上目前是第幾幀
    draw.text((10, 10), f"Frame {i + 1}/{TOTAL_FRAMES}", fill=(255, 255, 255))

    # 3-6 把這張圖加進影片
    writer.append_data(np.array(img))   # 先把圖轉成數字陣列，imageio 才吃得下

# ===== 4. 收尾：關閉檔案，影片才會存好 =====
writer.close()
print("完成！影片已存成 my_video.mp4")
