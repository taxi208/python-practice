import pandas as pd

# ✅ 正しいファイル名
df = pd.read_csv("outputs/sales_data.csv")


# 列名を確認
print("列名一覧:", df.columns)

# 合計計算
# わざと列名を間違える
total = df["sales"].sum()
print("合計は:", total)

