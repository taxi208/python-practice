import plotly.express as px

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

# === 5. Plotlyで上位10件の棒グラフを作成 ===
fig = px.bar(
    top10,
    x="date",          # ← CSVの列名に合わせる
    y="sales",         # ← 同じく列名どおり
    title="上位10件の売上ランキング",
    color="sales",
    color_continuous_scale="Oranges"
)

# HTMLに出力
fig.write_html("outputs/top_sales_plot.html")

print("✅ 上位10件のグラフを出力しました → outputs/top_sales_plot.html")
