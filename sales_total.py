import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import webbrowser

# CSV読み込み
df = pd.read_csv("sales_data.csv")

# 日付をdatetime型に変換
df["date"] = pd.to_datetime(df["date"])

# ==== Matplotlib（静的グラフ） ====
# 日別売上折れ線＋平均線
plt.figure(figsize=(8, 5))
plt.plot(df["date"], df["sales"], marker="o", label="売上（折れ線）", color="blue")
plt.bar(df["date"], df["sales"], alpha=0.3, label="売上（棒グラフ）", color="skyblue")
plt.axhline(y=df["sales"].mean(), color="red", linestyle="--", label="平均")

plt.title("日別売上の推移")
plt.xlabel("日付")
plt.ylabel("売上金額")
plt.legend()
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.close()

print("✅ Matplotlib版グラフ『sales_chart.png』を保存しました！")

# ==== 月別売上グラフ ====
df["month"] = df["date"].dt.to_period("M")
monthly_sales = df.groupby("month")["sales"].sum()

monthly_sales.plot(kind="bar", color="orange", figsize=(8, 5))
plt.title("月別売上（合計）")
plt.xlabel("月")
plt.ylabel("売上合計")
plt.tight_layout()



plt.savefig("outputs/sales_monthly_chart.png")
plt.close()



print("✅ 月別売上グラフ『sales_monthly_chart.png』を保存しました！")

# ==== Plotly（動くグラフ） ====
pio.renderers.default = "browser"

fig = px.line(
    df,
    x="date",
    y="sales",
    title="📈 日別売上グラフ（Plotly版）",
    markers=True
)

fig.update_traces(mode="lines+markers")  # 点を表示
fig.update_layout(template="plotly_white")  # 背景を白に
fig.show()  # その場でグラフを開く


# HTML出力して自動でブラウザ表示
fig.write_html("outputs/sales_plot.html")
webbrowser.open("sales_plot.html")
print("🌈 sales_plot.html をブラウザで開きました！")
