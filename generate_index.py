# generate_index.py
import datetime
import os

# === ファイルパス設定 ===
output_dir = "outputs"
docs_dir = "docs"
index_html = os.path.join(docs_dir, "index.html")
# === HTML構築 ===
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>📊 売上ダッシュボード</title>
    <style>
        body {{
            font-family: "Hiragino Sans", sans-serif;
            margin: 30px;
            background-color: #f5f7fa;
            color: #333;
        }}
        h1 {{
            color: #007acc;
        }}
        .updated {{
            color: #666;
            font-size: 14px;
        }}
        iframe {{
            width: 100%;
            height: 420px;
            border: 1px solid #ccc;
            border-radius: 8px;
            margin-bottom: 25px;
            background: #fff;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ccc;
            margin: 40px 0;
        }}
    </style>
</head>
<body>
    <h1>📊 売上ダッシュボード</h1>
    <p class="updated">最終更新日時：{now}</p>

    
<h2>① 全体売上グラフ</h2>
<iframe src="./sales_plot.html"></iframe>

<h2>② 上位10件ランキング</h2>
<iframe src="./top_sales_plot.html"></iframe>
<hr>
<p>✅ 自動生成 by auto_sales_report.py</p>
</body>
</html>
"""

# === ファイル出力 ===
os.makedirs(docs_dir, exist_ok=True)
with open(index_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ index.html を生成しました → {index_html}")
