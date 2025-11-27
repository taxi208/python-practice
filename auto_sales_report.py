# === auto_sales_report.py ===
# ChatGPT転職カリキュラム / プロ仕様バージョン
# 売上レポートを一括生成 → HTML生成 → Slack通知 → メール送信まで行うスクリプト
# このバージョンは logging を全面的にプロ仕様に改良したもの
# 作成: issey / 2025ポートフォリオ用

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
import json

# === ロガー設定読み込み ===
from logger_setup import setup_logger
logger = setup_logger()

# === 0. .env読み込み ===
load_dotenv()


# === 1. 汎用スクリプト実行関数 ===
def run_script(script_name):
    logger.info(f"▶ 実行開始: {script_name}")
    start = time.time()

    try:
        subprocess.run(["python", script_name], check=True)
        elapsed = round(time.time() - start, 2)
        logger.info(f"🟩 成功: {script_name}（{elapsed}秒）")
        return True
    except Exception as e:
        logger.error(f"❌ 失敗: {script_name} → {e}", exc_info=True)
        return False


# === 2. Slack通知（必要ならONにできる） ===
def send_slack(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    if not webhook_url:
        logger.warning("Slack Webhook URL 未設定のため通知スキップ")
        return

    try:
        response = requests.post(webhook_url, json={"text": message})
        if response.status_code == 200:
            logger.info("Slack通知成功")
        else:
            logger.error(f"Slack通知エラー: {response.status_code}")
    except Exception as e:
        logger.error(f"Slack送信に失敗: {e}", exc_info=True)


# === 3. メール送信（send_mail.pyの関数を使用） ===
from send_mail import send_report_via_email


# === 4. メイン処理 ===
def main():
    logger.info("====== 自動レポート生成開始 ======")
    start_total = time.time()

    # 実行するスクリプト一覧
    scripts = [
        "sales_total.py",
        "high_sales.py",
        "generate_index.py"
    ]

    all_success = True

    # --- 各スクリプト実行 ---
    for script in scripts:
        if not run_script(script):
            all_success = False

    # --- 最終ログ ---
    if all_success:
        msg = "🟩 全スクリプト正常完了！"
        logger.info(msg)
        send_slack(msg)
    else:
        msg = "⚠ 一部スクリプトに失敗が発生しました"
        logger.error(msg)
        send_slack(msg)

    # --- JSONログ保存（エビデンス的に強い） ---
    log_data = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success" if all_success else "error",
        "executed_scripts": scripts,
        "attachments": ["sales_chart.png", "top_sales_plot.html"]
    }

    with open("report_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data, ensure_ascii=False) + "\n")

    # --- 全体処理時間 ---
    total_elapsed = round(time.time() - start_total, 2)
    logger.info(f"====== 自動レポート生成終了（処理時間: {total_elapsed}秒）======")


    # === 5. メール送信 ===
    load_dotenv()

    email_files = [
        "outputs/sales_chart.png",
        "outputs/top_sales_plot.html"
    ]

    try:
        send_report_via_email(
            attachments=email_files,
            sender=os.getenv("EMAIL_SENDER"),
            receiver=os.getenv("EMAIL_RECEIVER")
        )
        logger.info("📧 メール送信完了")
    except Exception as e:
        logger.error(f"メール送信でエラー発生: {e}", exc_info=True)


# === 実行 ===
if __name__ == "__main__":
    main()
