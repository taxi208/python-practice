# 👋 Hi, I'm isse / taxi208

こんにちは、いっせい（taxi208）です。

2024年8月末に VSCode と GitHub を導入し、同じ頃に ChatGPT と出会いました。  
タクシーの仕事中に道路標識について質問した際、即レスで答えが返ってきて

**「プログラミングって僕でもできるん？もう遅い？」**

と聞いたところ、ChatGPT の『できます。』の一言で火がつきました。  
隔日勤務の合間に毎日少しずつ積み上げ、学習を継続しています。

---

## 🚀 Skills / 使用技術

**Python**
- pandas（CSV処理 / 集計 / 可視化）
- matplotlib / Plotly
- Flask（Webアプリ）

**その他**
- Git & GitHub（Pages含む）
- 自動化スクリプト
- HTML/CSS（基礎）

---

## 📚 Main Projects / 主なプロジェクト

### 📊 1. 売上分析・自動レポート生成ツール（Python）
CSV読込 → 集計 → 可視化 → 自動レポート生成まで行う実践ツール。

- 日次・月次レポート生成  
- 上位売上ランキング抽出  
- Slack通知 / メール通知  
- GitHub Pagesでレポート公開

👉 リポジトリ: https://github.com/taxi208/python-practice

---

### 🌐 2. Flask フォーム送信アプリ
HTMLフォーム → Pythonで処理 → テンプレ返却のWebアプリ。

---

### 🧪 3. エラー練習シリーズ
基本文法・デバッグ練習用のスクリプト集。

---

## 🎯 Goals / 目標
- プロジェクトを5つ公開  
- FlaskでWebアプリを完成  
- paiza C→Bランクへ  
- **5ヶ月以内にエンジニア転職**

---

## 🔥 Mindset
- 小さなコミットでも“毎日積み上げる”
- 1日1時間の学習を継続
- ショートカットや基礎力を固める
- ChatGPTを使い倒して最速で成長する

---

## 👤 About Me / 自己紹介

ChatGPTと出会って初めて「プログラミングが自分にもできるかもしれない」と感じました。  
隔日勤務の合間に独学しながら、小さく前進を積み上げています。

---

## 📫 Contact
X（Twitter）：準備中

---

**このアカウントでは、学習の成果や改善を継続的に公開していきます。**  
エンジニアとしての最初の1歩を、ここから踏み出します。🔥

---

## 💬 補足
Weather App・自動売上レポートなどの詳細は  
→ **各プロジェクトの README に記載**
## 📝 Update / 本日のアップデート（2025-11-22）

### 🔧 自動レポート生成ツール（auto_sales_report.py）
- 転職用のプロフェッショナル構成に全面リファクタリング  
- `run_script()` を新規実装し、  
  - スクリプト実行の共通化  
  - 実行時間計測  
  - 例外処理（try/except）  
  を標準化  
- INFO / ERROR ログを統一し、`logging` による正式ログ出力へ移行  
- `report_log.txt`（テキストログ）と  
  `report_log.json`（構造化ログ）の自動生成に対応  
- Slack 通知処理に例外対策を追加し、Webhook 未設定時は安全にスキップする仕様へ改善  
- `.env` 読み込み（python-dotenv）を導入し、環境変数で設定管理できる構造に改良  

### 🛠 Mac / VSCode / venv 関連の問題解決
- Homebrew 版 Python の仕様により  
  `pip` / `python` がターミナルで認識されない問題を解決  
- venv が VSCode 上で見えていても  
  実際はシステム Python が動いてしまう現象を解消  
- `source venv/bin/activate` により仮想環境を正しく有効化  
- `./venv/bin/python3 -m pip install python-dotenv` を使用し  
  venv 内へ確実に python-dotenv をインストール  
- `python-dotenv` インストール済みなのに  
  `No module named 'dotenv'` が出る原因を特定し、完全解決  

### 📊 各スクリプト実行（すべて成功）
- `sales_total.py`  
  - 日次 / 月次売上レポート生成  
  - グラフ画像（PNG）正常出力  
- `high_sales.py`  
  - 上位売上抽出  
  - プロット HTML 出力  
- `generate_index.py`  
  - docs/index.html を正常更新  
- 全スクリプトが `auto_sales_report.py` からワンクリック自動実行で流れる状態を実現  
- Slack 通知も完了  

### ✅ 結果
- 「売上分析〜HTML生成〜通知までを自動化するバックエンドツール」を  
  **転職ポートフォリオで提出できる品質まで引き上げ完了**  
- 実務でも使用できるレベルの  
  **ログ管理 / エラー処理 / 例外ハンドリング / 設定管理** が身についた  
- Mac + VSCode + venv の環境トラブルを自力で解決できるスキルを獲得  
- GitHub に公開して問題ない構成へアップデート完了


