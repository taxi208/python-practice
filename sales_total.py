import matplotlib
matplotlib.use("MacOSX")  # Mac用
import matplotlib.pyplot as plt

# sales_data.txt を読み込む
sales_input = []
with open("sales_data.txt", encoding="utf-8") as f:
    for line in f:
        s = line.strip().replace(",", "")
        if s.isdigit():  # 数字だけなら追加
            sales_input.append(int(s))

# 平均計算
avg_input = sum(sales_input) / len(sales_input)

# グラフ作成
plt.bar(range(len(sales_input)), sales_input, label="売上")
plt.axhline(y=avg_input, color="red", linestyle="--", label="平均")
plt.title("売上一覧")
plt.legend()
plt.tight_layout()
plt.savefig("sales_chart.png")  # ← PNGで保存
print("✅ sales_chart.png を保存しました")

plt.rcParams["font.family"] = "Hiragino Sans"
plt.rcParams["axes.unicode_minus"] = False