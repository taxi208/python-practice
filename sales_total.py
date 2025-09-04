# sales_total.py
sales = [10000, 20000, 1897, 8200, 13300]

total = sum(sales)
avg = total / len(sales)

print(f"件数: {len(sales)}")
print(f"合計: {total:,} 円")
print(f"平均: {avg:,.0f} 円")
print("合計金額の計算が完了しました！")
cd ~/Python/python-practice   # あなたの sales_total.py が入ってるフォルダへ移動