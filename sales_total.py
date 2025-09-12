import matplotlib
matplotlib.use("MacOSX")  # Mac用
import matplotlib.pyplot as plt

# # sales_data.txt を読み込む
# #sales_input = []
# with open("sales_data.txt", encoding="utf-8") as f:
#     for line in f:
#         s = line.strip().replace(",", "")
#         if s.isdigit():  # 数字だけなら追加
#             sales_input.append(int(s))

# # 平均計算
# avg_input = sum(sales_input) / len(sales_input)

# # グラフ作成
# plt.bar(range(len(sales_input)), sales_input, label="売上")
# plt.axhline(y=avg_input, color="red", linestyle="--", label="平均")
# plt.title("売上一覧")
# plt.legend()
# plt.tight_layout()
# plt.savefig("sales_chart.png")  # ← PNGで保存
# print("✅ sales_chart.png を保存しました")

plt.rcParams["font.family"] = "Hiragino Sans"
plt.rcParams["axes.unicode_minus"] = False
import pandas as pd

# CSVを読み込む
df = pd.read_csv("sales_data.csv")

print(df)
print("合計:", df["sales"].sum())
print("平均:", df["sales"].mean())
# グラフ描画
import matplotlib.pyplot as plt

plt.bar(df["day"], df["sales"], label="売上")
plt.axhline(df["sales"].mean(), color="red", linestyle="--", label="平均")
plt.xlabel("日")
plt.ylabel("売上")
plt.title("売上グラフ")
plt.legend()
plt.tight_layout()
plt.savefig("sales_chart.png")  # PNGで保存
plt.show()
import pandas as pd

# CSVを読み込む
df = pd.read_csv("sales_data.csv")

# データ確認
print("データ一覧：")
print(df)

# 売上の合計
total = df["sales"].sum()
print("売上合計:", total)

# 売上の平均
avg = df["sales"].mean()
print("平均売上:", avg)

# 最大・最小もついでに出す
max_value = df["sales"].max()
min_value = df["sales"].min()
print("最大売上:", max_value)
print("最小売上:", min_value)
# ===== 並び替え =====
print("\n売上が多い順に並び替え：")
sorted_df = df.sort_values("sales", ascending=False)
print(sorted_df)
# 売上が1万以上の日を抽出
print("\n売上が1万以上の日：")
high_sales = df[df["sales"] >= 10000]
print(high_sales)
# CSVに保存
high_sales.to_csv("high_sales.csv", index=False)
print("high_sales.csv に保存しました！")

