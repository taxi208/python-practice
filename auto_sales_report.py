# === auto_sales_report.py ===
# ChatGPT最強カリキュラム / Python × HTMLレポート × Slack通知 × メール送信で行うフル自動レポート
# このバージョンは Logging 全強化版（クラッシュしても内容が全部残る）
# 作者：issey / 2025ポートフォリオ用

import subprocess
import time
import datetime
import os
import logging
import requests
from dotenv import load_dotenv

# === 0. .env読み込み ===
load_dotenv()

# === ロガー設定読み込み ===
from logger_setup import setup_logger
logger = setup_logger()

# === 1. 汎用スクリプト実行関数 ===
def run_script(script_name):
    logger.info(f"▶️ 実行開始：{script_name}")
    start = time.time()

    try:
        subprocess.run(["python", script_name], check=True)
        elapsed = round(time.time() - start, 2)
        logger.info(f"✅ 成功：{script_name}（{elapsed}秒）")
        return True
    except Exception as e:
        logger.error(f"❌ 失敗：{script_name} → {e}", exc_info=True)
        return False

# === 2. Slack通知（Block Kit） ===
def send_slack(title, color, details=None):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    if not webhook_url:
        logger.warning("Slack Webhook URL 未設定 → 通知スキップ")
        return

    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{color} {title}*"
            }
        }
    ]

    if details:
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"```{details}```"
            }
        })

    payload = {"blocks": blocks}

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            logger.info("Slack通知送信成功")
        else:
            logger.error(f"Slack通知エラー：{response.status_code}")
    except Exception as e:
        logger.error(f"Slack送信で例外発生：{e}")

# === 3. メール送信 ===
from send_mail import send_report_via_email

def main():
    try:
        logger.info("====== 自動レポート生成開始 ======")
        start_total = time.time()

        # 実行するスクリプト一覧
        scripts = [
            "sales_total.py",
            "high_sales.py",
            "generate_index.py",
        ]

        all_success = True

        # --- 各スクリプト実行 ---
        for script in scripts:
            if not run_script(script):
                all_success = False

        # --- 最終ログ ---
        if all_success:
            msg = "全スクリプト正常完了！"
            logger.info(msg)
            send_slack(
                title="🟩 全スクリプト正常完了",
                color="good",
                details=msg
            )
        else:
            msg = "⚠️ 一部スクリプトに失敗が発生しました"
            logger.error(msg)
            send_slack(
                title="⚠️ 一部スクリプト失敗",
                color="warning",
                details=msg
            )

        total_elapsed = round(time.time() - start_total, 2)
        logger.info(f"====== 自動レポート生成終了（処理時間：{total_elapsed}秒）======")

        # === 5. メール送信 ===
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
            logger.error(f"メール送信でエラー発生：{e}", exc_info=True)

    except Exception as e:
        logger.error(f"🔥 メイン処理で致命的エラー：{e}", exc_info=True)
        send_slack(title="🔥 メイン処理で致命的エラー", color="danger", details=str(e))

# === 実行 ===
if __name__ == "__main__":
    main()

