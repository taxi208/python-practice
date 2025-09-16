# python-practice

このリポジトリはPython学習用です。  
毎日少しずつコードを書き、学習の記録を残していきます。

## 進捗メモ
- 2025-09-04: sales_total.py を作成。売上の合計と平均を計算できるようになった。
- これからはPythonの基礎（if文, for文, 関数）を学ぶ予定。
# Python Practice - Graph

このリポジトリは、Python学習の記録用です。  
基礎文法の練習から始め、グラフ描画やデータ処理を通じてスキルアップを目指しています。

## 含まれる内容
- `sales_total.py` : 売上の合計・平均を計算するコード
- `sales_data.txt` : 練習用の売上データ
- `sales_chart.png` : グラフ描画のサンプル出力

## 学習の進捗
- Pythonの基本文法
- グラフ描画（matplotlib）
- データ集計の基礎
- 今後は CSV / pandas を使ったデータ処理へ進む予定
- 2025-09-11: pandasでCSV集計とグラフ描画ができるようになった
## 進捗メモ

- 2025-09-13: `sales_total.py` を関数化  
  - `extract_high_sales` 関数を追加  
  - 閾値を自由に変更可能に改良  
  - 出力メッセージを動的に修正
## 進捗メモ
git commit -m "進捗メモをREADMEに追記 (関数化と閾値対応)"
# python-practice

このリポジトリでは、Pythonを使ったデータ処理と可視化の練習を行っています。  
CSVファイルから日別売上を集計し、折れ線グラフとして表示。さらに平均線を追加して、売上の傾向を視覚的に確認できるようにしました。  

## 使用技術
- Python 3.9
- pandas
- matplotlib

## 実行方法
```bash
python3 sales_total.py
```

## 実行結果の例
![日別売上の推移](sales_line_chart.png)

