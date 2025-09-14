import pandas as pd

# CSVを読み込む
data = pd.read_csv("sales_data.csv")

# 列名と先頭を確認
print(data.head())             # データの先頭5行
print(data.columns.tolist())   # 列名リスト


# --- この下から分析処理を書いてOK ---
daily_sales = data.groupby("day")["sales"].sum()
print(daily_sales)


# CSVを読み込む
data = pd.read_csv("sales_data.csv")

# データ確認
print(data.head())            # 先頭5行
print(data.columns.tolist())  # 列名リスト



def extract_high_sales(input_file, output_file, threshold=10000):
    # CSV読み込み
    df = pd.read_csv(input_file)

    # 条件でフィルタリング
    high_sales = df[df['sales'] >= threshold]

    # CSV保存
    high_sales.to_csv(output_file, index=False)

    print(f"売上{threshold}以上のデータを {output_file} に保存しました。")



# 実行例
if __name__ == "__main__":

    extract_high_sales("sales_data.csv", "high_sales.csv", threshold=20000)
if __name__ == "__main__":
    # 高売上データを抽出
    extract_high_sales("sales_data.csv", "high_sales.csv", 50000)

    # グラフ描画
    import pandas as pd
    import matplotlib.pyplot as plt
    daily_sales = data.groupby("day")["sales"].sum()


    plt.figure(figsize=(8,5))
    plt.plot(daily_sales.index, daily_sales.values, marker="o")
    plt.title("日別売上の推移")
    plt.xlabel("日付")
    plt.ylabel("売上金額")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sales_line_chart.png")
    plt.show()


