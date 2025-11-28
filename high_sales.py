# high_sales.py
import pandas as pd
import plotly.express as px
from pathlib import Path


def generate_high_sales_report():
    # === 1. パス設定 ===
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "outputs" / "sales_data.csv"
    output_csv = base_dir / "outputs" / "high_sales.csv"

    output_html = base_dir / "outputs" / "top_sales_plot.html"

    # === 2. データ読み込み ===
    df = pd.read_csv(data_path)

    # === 3. 売上トップ10 ===
    df_sorted = df.sort_values(by="sales", ascending=False)
    top10 = df_sorted.head(10)

    # === 4. CSVに保存 ===
    top10.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"✔ high_sales.csv を出力しました → {output_csv}")

    # === 5. Plotly インタラクティブ棒グラフ ===
    fig = px.bar(
        top10,
        x="date",
        y="sales",
        color="sales",
        title="上位10件の売上ランキング",
        color_continuous_scale="Oranges",
        text_auto=True,
    )

    fig.update_layout(
        xaxis_title="日付",
        yaxis_title="売上",
        template="plotly_white",
        title_font=dict(size=22),
        xaxis_tickangle=-30,
    )

    # === 6. HTML に書き出し ===
    fig.write_html(output_html)
    print(f"✔ 上位10件グラフを出力しました → {output_html}")

    return output_html

if __name__ == "__main__":
    # TODO: 本番のレポート作成（今はコメントアウト）
      generate_high_sales_report()

    # === Plotlyテスト ===
# import plotly.express as px
# import pandas as pd

    # df = pd.DataFrame({
    #     "商品名": ["A", "B", "C"],
    #     "売上": [100, 200, 150]
    # })

    # fig = px.bar(df, x="商品名", y="売上", title="Plotlyテスト")
    # fig.show()

