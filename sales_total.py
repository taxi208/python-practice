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

if a != b and b >= c:
    print("OK")

