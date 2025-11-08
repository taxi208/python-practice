## 🧠 プロジェクト概要

このリポジトリは、売上データを自動で集計・可視化し、
レポートをGmail経由で送信する「自動レポート生成システム」です。

**目的：**
- Pythonスクリプトによる業務自動化の実践
- logging / subprocess / smtplib など、実務で使われる標準モジュールの理解
- `.env`を用いた環境変数管理とセキュリティ対応

**想定シーン：**
- 毎日定時に売上報告を自動生成して上司へメール送信
- クラウドや共有ドライブへ自動出力

# python-practice
（システム名の位置にタイトルだけ残す）


このリポジトリは、Python を使った売上データの集計と可視化の練習用です。  
日別売上をグラフ化し、平均線・ランキング出力・合計/平均の算出まで行いました。

---

Pythonを使って売上データを自動集計・可視化する練習プロジェクトです。  
日別・月別の売上グラフや、上位ランキングのCSV出力を自動生成します。

---

## 🧰 使用技術
- Python 3.9
- pandas
- matplotlib
- plotly
- GitHub Pages

---

## 🚀 実行方法

```bash
python3 sales_total.py

---

## 📈 売上グラフ（サンプル）

![日別売上グラフ](https://raw.githubusercontent.com/taxi208/python-practice/main/outputs/sales_chart.png)

---

## 📊 最後の確認：画像埋め込みテスト

<img src="https://raw.githubusercontent.com/taxi208/python-practice/main/outputs/sales_chart.png" width="600">

---

## 🏆 上位10件の売上ランキング（Plotly版）

`high_sales.py` を実行すると、売上データから上位10件を抽出し、
インタラクティブな棒グラフ（`outputs/top_sales_plot.html`）を自動生成します。

```bash
python3 high_sales.py

---

## 🌐 公開ページ（GitHub Pages）
[▶ グラフを見る（GitHub Pages版）](https://taxi208.github.io/python-practice/)

---

## 🤖 自動売上レポート（完全自動化）

`auto_sales_report.py` を実行すると、  
以下の処理がすべて自動で行われます。

- 各スクリプト（`sales_total.py`, `high_sales.py`, `generate_index.py`）を順に実行  
- `report_log.txt` に実行ログを記録  
- `.env` からGmailパスワードを安全に読み込み  
- 最新グラフ（PNG / HTML）をメールに添付して送信  

```bash
python3 auto_sales_report.py

## 🧩 実行結果メモ（2025-11-06）
- ✅ 売上レポート自動生成完了（Python 3.13.7, macOS）
- ✅ Gmail通知・添付ファイル送信確認済み
- 出力ファイル：
  - `outputs/sales_chart.png`
  - `outputs/top_sales_plot.html`
- スクリーンショット：
  - `/images/report_terminal.png`
  - `/images/report_mail.png`
Slack通知A+版の実装
✅ Slack通知A＋版の実装  
- 総売上金額と売上件数をSlackメッセージ内に表示  
- 成功時は緑色（#36a64f）で通知  
- 出力リンク（グラフ／ランキング）を自動添付

