# === auto_sales_report.py ===
# 🧩 ChatGPTカリキュラム転職対応版
# 売上レポート自動生成・ログ出力・メール通知までを全自動で実行するスクリプト
# （開発者：issey / 2025年版ポートフォリオ対応）

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

# === 0. 環境変数の読み込み ===
load_dotenv()

# === 1. ログ設定 ===
logging.basicConfig(
    filename="report_log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log(msg):
    """ログ出力＋ターミナル表示"""
    print(msg)
    logging.info(msg)

def log_success(script_name, elapsed):
    log(f"✅ {script_name} 実行成功（{elapsed:.2f}秒）")

def log_error(script_name, error):
    log(f"❌ {script_name} 実行失敗: {error}")

# === 2. スクリプト実行関数 ===
def run_script(script_name):
    """個別スクリプトを安全に実行し、時間を計測"""
    start = time.time()
    log(f"▶ {script_name} 実行開始")
    try:
        subprocess.run(["python", script_name], check=True)
        elapsed = time.time() - start
        log_success(script_name, elapsed)
    except subprocess.CalledProcessError as e:
        log_error(script_name, e)
        raise SystemExit("処理を中断しました。")

# === 3. 各スクリプト順次実行 ===
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log(f"\n🧮 売上レポート自動生成開始：{now}\n" + "=" * 60)

run_script("sales_total.py")
run_script("high_sales.py")
run_script("generate_index.py")

end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log(f"\n📊 売上レポート自動生成完了：{end}\n" + "=" * 60)

# === 4. メール送信関数 ===
def send_report_via_email(attachments, sender, password, receiver):
    """自動生成されたレポートをメール送信"""
    try:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = "📈 売上レポート自動生成完了通知"
        body = f"売上レポートが正常に生成されました。\n完了時刻：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        msg.attach(MIMEText(body, "plain", "utf-8"))

        # 添付ファイルを追加
        for file_path in attachments:
            with open(file_path, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
                part["Content-Disposition"] = f'attachment; filename="{os.path.basename(file_path)}"'
                msg.attach(part)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)

        log("📧 メール送信成功！")

    except Exception as e:
        log(f"⚠️ メール送信失敗: {str(e)}")

# === 5. メール送信を実行 ===
sender = "issey.rickowens@gmail.com"
password = os.getenv("EMAIL_PASSWORD")
receiver = "issey.rickowens@gmail.com"

attachments = [
    "outputs/sales_chart.png",
    "outputs/top_sales_plot.html"
]

send_report_via_email(attachments, sender, password, receiver)
log("✅ 自動処理がすべて完了しました！\n")

