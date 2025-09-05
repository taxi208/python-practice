# 売上を判定する関数
# mode が "avg" のときは平均値で判定
# mode が "threshold" のときは任意の基準値で判定
def judge_sales(sales, mode="avg", threshold=None):
    if mode == "avg":
        avg = sum(sales) / len(sales)
        print(f"平均は {avg:,.0f} 円です")
        for s in sales:
            if s >= avg:
                print(f"{s:,}円 → 平均以上！よくできました！")
            else:
                print(f"{s:,}円 → 平均未満…次がんばろう！")
    elif mode == "threshold":
        if threshold is None:
            print("基準値が指定されていません")
            return
        print(f"基準値は {threshold:,} 円です")
        for s in sales:
            if s >= threshold:
                print(f"{s:,}円 → 基準以上！よくできました！")
            else:
                print(f"{s:,}円 → 基準未満…次がんばろう！")

# メイン処理
sales = [10000, 20000, 1897, 8200, 13300]

# 平均で判定
print("=== 平均で判定 ===")
judge_sales(sales, mode="avg")

# 任意の基準値（1万円）で判定
print("\n=== 基準値で判定 ===")
judge_sales(sales, mode="threshold", threshold=10000)

