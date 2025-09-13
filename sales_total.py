import pandas as pd

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


