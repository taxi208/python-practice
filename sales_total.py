import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'  # Mac用フォント設定

import plotly.express as px
import plotly.io as pio
import webbrowser

# === データ読み込み ===
df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# === Matplotlib（日別グラフ） ===
plt.figure(figsize=(8, 5))
plt.plot(df["date"], df["sales"], marker="o", label="売上（折れ線）", color="blue")
plt.bar(df["date"], df["sales"], alpha=0.3, label="売上（棒グラフ）", color="skyblue")
plt.axhline(y=df["sales"].mean(), color="red", linestyle="--", label="平均")

plt.title("📊 日別売上の推移")
plt.xlabel("日付")
plt.ylabel("売上金額")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/sales_chart.png")
plt.close()
print("✅ Matplotlib版グラフ『sales_chart.png』を保存しました")

# === 月別集計 ===
df["month"] = df["date"].dt.to_period("M")
monthly_sales = df.groupby("month")["sales"].sum()

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="bar", color="orange")
plt.title("📅 月別売上（合計）")
plt.xlabel("月")
plt.ylabel("売上金額")
plt.tight_layout()
plt.savefig("outputs/sales_monthly_chart.png")
plt.close()
print("✅ 月別売上グラフ『sales_monthly_chart.png』を保存しました")

# === Plotly（インタラクティブ） ===
pio.renderers.default = "browser"
fig = px.line(
    df,
    x="date",
    y="sales",
    title="📈 日別売上グラフ（Plotly版）",
    markers=True
)
fig.update_traces(mode="lines+markers")
fig.update_layout(template="plotly_white")


fig.write_html("outputs/sales_plot.html")
webbrowser.open("outputs/sales_plot.html")
print("🌈 sales_plot.html をブラウザで開きました！")
