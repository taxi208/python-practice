# high_sales.py
import pandas as pd

# === 1. データ読み込み ===
df = pd.read_csv("outputs/sales_data.csv")

# === 2. 売上の降順で並べ替え ===
df_sorted = df.sort_values(by="sales", ascending=False)

# === 3. 上位10件を抽出 ===
top10 = df_sorted.head(10)

# === 4. CSV出力 ===
output_file = "high_sales.csv"
top10.to_csv(output_file, index=False, encoding="utf-8-sig")

print("✅ high_sales.csv を出力しました！")

