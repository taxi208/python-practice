# 売上データをファイルから読み込みたい
file_path = "sales_data.csv"

with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()

print("ファイルの内容:")
print(data)
