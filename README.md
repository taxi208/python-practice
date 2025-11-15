# python-practice 🐍📊  
売上データを自動集計し、グラフ生成・上位ランキング作成・  
レポートを自動作成する「自動レポート生成システム」です。

---

## 📌 プロジェクト概要

Pythonを使って、売上データの集計・可視化・自動化を行う実践プロジェクトです。
以下の処理をまとめて自動化し、日別/月別の売上レポートを自動作成します。

### 🔧 主な機能
- Pythonスクリプトによる売上集計処理
- 折れ線グラフ / ランキング表 / HTMLレポートの自動生成
- logging / subprocess / SMTP / .env の基本操作を習得
- ローカルでの実行（macOS）
- Gmail の SMTP を使ったメール送信
- 画像・HTMLファイルの一括出力
- GitHub Pages への成果物公開

---

## 🗂 ディレクトリ構成

```txt
python-practice/
├── sales_total.py
├── high_sales.py
├── generate_index.py
├── auto_sales_report.py
├── error_practice_01.py
├── error_practice_02.py
├── error_practice_03.py
├── error_practice_04.py
├── sales_data.csv
├── outputs/
│   ├── sales_chart.png
│   ├── top_sales_plot.html
│   ├── report_mail.png
│   └── sales_line_test.png
└── images/
    └── report_terminal.png


---

## 🧪 使用技術（Tech Stack）

- Python 3.9
- pandas
- matplotlib
- Plotly
- GitHub Pages

---

## 🚀 実行方法（基本）

### 売上集計（折れ線グラフ生成）
bash
python3 sales_total.py

---

## 📈 売上グラフ（サンプル）

![日別売上グラフ](https://raw.githubusercontent.com/taxi208/python-practice/main/outputs/sales_chart.png)

---

## 🥇 上位10件の売上ランキング（Plotly版）

売上データから上位10件を抽出し、
インタラクティブな棒グラフとして自動生成します（HTML出力）。

bash
python3 high_sales.py

出力先：`outputs/top_sales_plot.html`

---

## 🌍 公開ページ（GitHub Pages）
https://taxi208.github.io/python-practice/

---

## 📦 自動レポート作成（まとめて実行）

以下のメインスクリプトで各処理を一括実行できます。
bash
python3 auto_sales_report.py


### 🔄 実行される処理フロー
1. 売上集計（sales_total.py）
2. 上位10件ランキング（high_sales.py）
3. レポートHTML生成（generate_index.py）
4. 画像・CSV・HTMLを `/outputs` にまとめて保存
5. Gmail SMTPでメール送信
6. ログファイル（report_log.txt）を保存

---

## 🧪 練習セット（error_practice_01〜04）

### 練習セット3：エラー練習 & 可視化テスト（error_practice_04.py）

- pandas による CSV 読み込み
- matplotlib で日本語フォント設定（AppleGothic）
- `plt.savefig()` による画像書き出し

### 出力結果

![sales_line_test](https://raw.githubusercontent.com/taxi208/python-practice/main/outputs/sales_line_test.png)

生成スクリプト：`error_practice_04.py`
出力先：`/outputs/sales_line_test.png`

---

## 🔧 今後のアップデート予定

- README の画像埋め込みを整理
- `high_sales.py` の Plotly 対応（インタラクティブ棒グラフ）
- メール送信テンプレートを HTML化
- ログ強化（エラー検知 → Slack 通知）
- GitHub Actions による自動実行（CI/CD 化）

---

## 📄 ライセンス

MIT License  
本プロジェクトは自由に利用・改変できます。

---

## 📝 補足

このプロジェクトは、Python の基礎文法 → データ加工 → グラフ生成 → 自動化 → 公開  
までの流れを一通り実践するための学習用リポジトリです。

継続して改善を行い、業務自動化・データ分析スキルの向上を目的としています。

# Flaskフォーム送信アプリ

## ✅ やったこと
- Flask環境で簡単なフォームアプリを作成
- HTMLフォーム（form.html）で名前を入力し送信
- Python（hello_flask.py）でPOSTメソッドを受け取り、テンプレートへ渡す
- 結果を表示するindex.htmlの作成
- `localhost:5000` でフォーム確認＆動作確認成功！

## 💡 学び・ハマったこと
- `if request.method == "POST"` にインデントエラーで数回つまづいた
- `"=="` や `:` のあとにブロック（インデント）忘れ注意！
- 403エラーが出たときは、コードではなくブラウザのキャッシュや入力ミスの可能性あり
- フォームで日本語を扱うときもFlaskは問題なく対応可能

## 📂 実行方法
```bash
python hello_flask.py

---

## 📝 今日の学びと進捗（2025年11月15日）

- Flaskでフォームアプリを作成＆ローカル動作確認
- `POST`メソッドで名前入力→テンプレートで受け取り＆表示
- if文のインデントでエラーになったが、修正方法も習得
- 初めてのローカルサーバー起動成功 🎉
- READMEの更新、プロジェクトの整理完了💪


