import os

# 売上データをファイルから読み込みたい
file_path = "sales_data.csv"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    print("ファイルの内容:")
    print(data)
else:
    print(f"⚠️ ファイルが見つかりません: {file_path}")
    print("ファイル名・パスを確認してください。")
