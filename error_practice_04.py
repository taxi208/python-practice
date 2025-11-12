import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams

# 日本語フォント設定（macOSの場合）
rcParams["font.family"] = "AppleGothic"

# データ読み込み
df = pd.read_csv("outputs/sales_data.csv")

# 折れ線グラフ作成
plt.plot(df["date"], df["sales"], marker="o")
plt.title("日別売上グラフ")
plt.xlabel("日付")
plt.ylabel("売上")
plt.grid(True)

# ファイル保存
plt.savefig("outputs/sales_line_test.png")

# グラフ表示
# plt.show()
