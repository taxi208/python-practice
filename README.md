# python-practice 🧠💻

売上データを自動集計し、グラフ生成・上位ランキング作成・・・  
レポートを自動作成する「自動レポート生成システム」です。

---

## 🚀 プロジェクト概要

Python を使って、売上データの集計・可視化・自動化を行う実験プロジェクトです。  
以下の処理をまとめて自動化し、日別／月別の売上レポートを自動作成します。

### 🔧 主な機能
- Pythonスクリプトによる売上集計処理  
- 折れ線グラフ／ランキング表／HTMLレポートの自動生成  
- logging / subprocess / SMTP / .env の基本操作を習得  
- ローカルでの実行（macOS）  
- Gmail の SMTP を使ったメール送信  
- 画像・HTMLファイルの一括出力  
- GitHub Pages への成果物公開  

---

## 📁 ディレクトリ構成

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
```

---

## 🧰 使用技術（Tech Stack）

- Python 3.9  
- pandas  
- matplotlib  
- Plotly  
- GitHub Pages  

---

## ▶️ 実行方法（基本）

### 1. 売上集計（折れ線グラフ生成）
```bash
python3 sales_total.py
```

サンプル画像  
![日別売上グラフ](https://raw.githubusercontent.com/taxi208/python-practice/main/outputs/sales_chart.png)

---

### 2. 上位10件の売上ランキング（Plotly版）

```bash
python3 high_sales.py
```

**出力先：** `outputs/top_sales_plot.html`

---

### 3. 🔗 公開ページ（GitHub Pages）

https://taxi208.github.io/python-practice/

---

### 4. 自動レポート作成（まとめて実行）

```bash
python3 auto_sales_report.py
```

#### 実行される処理フロー
1. 売上集計（sales_total.py）  
2. 上位売上ランキング（high_sales.py）  
3. レポートHTML作成（generate_index.py）  
4. 画像・CSV・HTMLを `outputs` にまとめて保存  
5. Gmail SMTPメール送信  
6. ログファイル（report_log.txt）を保存  

---

## 🧪 練習セット（error_practice_01〜04）

### 練習セット03：エラー擬似＆可視化テスト（error_practice_04.py）

- pandas による CSV 読み込み  
- matplotlib で日本語フォント設定（AppleGothic）  
- `plt.savefig()` による画像書き出し  

出力画像  
![sales_line_test](https://raw.githubusercontent.com/taxi208/python-practice/main/outputs/sales_line_test.png)

---

## 📈 今後のアップデート予定

- README の画像読み込み改善  
- high_sales.py の Plotly 対応（インタラクティブ棒グラフ）  
- メール添付ファイル整理・HTML化  
- エラー検知（Slack 通知）  
- GitHub Actions による自動実行（CI/CD 化）

---

## 📜 ライセンス

MIT License  
本プロジェクトは自由に利用・改変できます。

---

## 🎯 まとめ

このプロジェクトは、Python の基礎文法・データ加工・グラフ生成・自動化・公開・・・  
までの流れを一通り実践するための学習用リポジトリです。

基礎を丁寧に積み、業務改善にも・データ分析スキルの向上を目的としています。

---

## 🧪 Flaskフォーム送信アプリ

### ✔️ やったこと
- Flask基礎：簡単なフォームアプリを作成  
- HTMLフォーム（form.html）で値を入力し送信  
- python（hello_flask.py）が POST メソッドで受け取り、テンプレートへ渡す  
- 結果表示する index.html の作成  
- `localhost:5000` でフォーム送信＆結果表示成功！

### ⚠️ 学び・ハマった点
- `if request.method == "POST"` にインデントミスで数回つまずいた  
- HTML → 変数 → 受け取り → ブロック（インデント）構造  
- 403エラーが出た時、コードではなくブラウザのキャッシュや入力ミスの可能性もあり  
- 一度エラー状態になると Flask が再起動まで効かない事例も経験  

### ▶️ 実行方法
```bash
python hello_flask.py
```

---

## 🔥 作者コメント（2025/11/15 時点）

- データ分析＆自動化の基礎が完成  
- Plotly のインタラクティブグラフまで実装  
- auto レポートの全体フロー構築  
- README 整理完了、プロジェクトの形が完成 💪
