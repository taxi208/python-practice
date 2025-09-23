# python-practice

このリポジトリは、Python を使った売上データの集計と可視化の練習用です。  
日別売上をグラフ化し、平均線・ランキング出力・合計/平均の算出まで行いました。

## 使用技術
- Python 3.9
- pandas
- matplotlib

## 実行方法
```bash
python3 sales_total.py
## 出力例
- sales_chart.png : 日別売上の折れ線グラフ
- high_sales.csv : 売上が指定値以上の日を抽出したCSV
- sales_line_chart.png : 売上データを折れ線グラフで表示したもの（平均線つき）
print("合計売上:", df["売上"].sum())

