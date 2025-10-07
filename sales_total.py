import pandas as pd
import matplotlib.pyplot as plt

# CSVを読み込み
df = pd.read_csv("sales_data.csv")

# 日別売上データ
daily_sales = df['sales']

# グラフ描画
plt.figure(figsize=(8, 5))
plt.plot(daily_sales.index, daily_sales.values, marker="o", label="売上（折れ線）")
plt.bar(df['day'], df['sales'], alpha=0.3, label="売上（棒グラフ）")

# 平均線を追加
plt.axhline(y=daily_sales.mean(), color="red", linestyle="--", label="平均")

plt.title("日別売上の推移")
plt.xlabel("日付")
plt.ylabel("売上金額")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.savefig("sales_line_chart.png")
plt.show()

# 高売上ランキング（TOP5）を抽出して保存
top_sales = df.sort_values(by="sales", ascending=False).head(5)
top_sales.to_csv("top_sales.csv", index=False)
print("高売上ランキングを top_sales.csv に保存しました！")

# 合計と平均を計算して表示
total_sales = df['sales'].sum()
mean_sales = df['sales'].mean()

print(f"売上合計: {total_sales}")
print(f"売上平均: {mean_sales:.2f}")
# 売上上位3日の抽出
top3 = df.sort_values(by="sales", ascending=False).head(3)
print("売上上位3日:")
print(top3)
if 1 != 2 and 3 == 3:
    print("OK")

# Fira Code 確認用
a = 1 != 2
b = 3 == 3
c = [1, 2, 3]
#d = c -> str  # Pythonではエラーになるけどフォント確認用

#if a != b and b >= c:
#    print("OK")



import pandas as pd

# CSVを読み込む
df = pd.read_csv("sales_data.csv")

# 基本的な集計
print("合計売上:", df["売上"].sum())
print("平均売上:", df["売上"].mean())
print("件数:", len(df))


# === 月別売上集計 ===
import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み（すでに上でやってる場合は省略OK）
df = pd.read_csv('sales_data.csv')

# 日付をdatetime型に変換
df['date'] = pd.to_datetime(df['date'])

# 月ごとに集計
df['month'] = df['date'].dt.to_period('M')
monthly_sales = df.groupby('month')['sales'].sum()

print("月別売上集計：")
print(monthly_sales)

# グラフ化
monthly_sales.plot(kind='bar')
plt.title('月別売上')
plt.xlabel('月')
plt.ylabel('売上金額')
plt.tight_layout()
plt.savefig('sales_monthly_chart.png')
plt.show()

# === 年別比較グラフ（前年比） ===
import matplotlib.pyplot as plt

# CSV読み込み
df = pd.read_csv("sales_data.csv")

# 年月をdatetime型に変換
df["date"] = pd.to_datetime(df["date"])

# 年と月を列として抽出
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

# 年月ごとの売上を集計
monthly_sales = df.groupby(["year", "month"])["sales"].sum().reset_index()

# ピボットテーブルで「月」を横軸、「年」を縦に並べる
pivot_sales = monthly_sales.pivot(index="month", columns="year", values="sales")

# グラフ描画
pivot_sales.plot(kind="bar", figsize=(10, 6))
plt.title("月別売上比較（前年・当年）", fontsize=14)
plt.xlabel("月")
plt.ylabel("売上額")
plt.legend(title="年度")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tigh

# === 年別比較グラフ（前年比） ===
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

monthly_sales = df.groupby(["year", "month"])["sales"].sum().reset_index()
pivot_sales = monthly_sales.pivot(index="month", columns="year", values="sales")

pivot_sales.plot(kind="bar", figsize=(10, 6))
plt.title("月別売上比較（前年・当年）", fontsize=14)
plt.xlabel("月")
plt.ylabel("売上額")
plt.legend(title="年度")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("sales_compare_year.png")
plt.show()

print("前年比較グラフを作成しました！📊 -> sales_compare_year.png")
