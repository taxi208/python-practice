# === auto_sales_report.py ===
# 🔥 ChatGPT転職カリキュラム：プロ仕様バージョン
# 売上レポート生成・上位売上抽出・HTML生成を全自動で行うスクリプト
# すべての処理を詳細にログ記録し、エラーにも対応
#（開発者：issey / 2025 ポートフォリオ用）

import subprocess
import datetime
import time
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import pandas as pd
import requests

# === 0. 環境変数の読み込み ===
load_dotenv()

# === 1. ログ設定 ===
logging.basicConfig(
    filename="report_log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log(msg):
    """ログを出力し、ターミナルにも表示"""
    print(msg)
    logging.info(msg)

def log_error(msg):
    """エラーをログとして記録"""
    print(f"[ERROR] {msg}")
    logging.error(msg)

# === 2. 汎用スクリプト実行関数 ===
def run_script(script_name):
    log(f"▶ 実行開始: {script_name}")
    start = time.time()

    try:
        subprocess.run(["python", script_name], check=True)
        elapsed = round(time.time() - start, 2)
        log(f"✅ 成功: {script_name}（{elapsed}秒）")
    except Exception as e:
        log_error(f"❌ 失敗: {script_name} → {e}")
        return False

    return True

# === 3. Slack通知（必要ならONにできる） ===
def send_slack(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        log("Slack Webhook URL が設定されていません。通知をスキップします。")
        return

    try:
        response = requests.post(webhook_url, json={"text": message})
        if response.status_code == 200:
            log("Slack通知: 成功")
        else:
            log_error(f"Slack通知エラー: {response.status_code}")
    except Exception as e:
        log_error(f"Slack送信に失敗: {e}")

# === 4. メール通知（後で実装予定） ===
def send_mail(subject, body, attachments=None):
    pass  # 転職後の実務フェーズで拡張

# === 5. メイン処理 ===
def main():
    log("====== 自動レポート生成開始 ======")

    scripts = [
        "sales_total.py",
        "high_sales.py",
        "generate_index.py",
    ]

    # 1つでも失敗したら False
    all_success = True

    for script in scripts:
        if not run_script(script):
            all_success = False

    # 最終ログ
    if all_success:
        msg = "✨ 全スクリプト正常完了！"
        log(msg)
        send_slack(msg)
    else:
        msg = "⚠ 一部スクリプトに失敗が発生しました"
        log_error(msg)
        send_slack(msg)

    log("====== 自動レポート生成終了 ======")

    # 実行ログをjson形式でも保存（エビデンスとして強い）
    log_data = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success" if all_success else "error",
        "executed_scripts": scripts,
        "attachments": ["sales_chart.png", "top_sales_plot.html"]
    }

    import json
    with open("report_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data, ensure_ascii=False) + "\n")

# === 実行 ===
if __name__ == "__main__":
    main()
