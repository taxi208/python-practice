# === auto_sales_report.py ===
import subprocess
import datetime
import os
import time
from dotenv import load_dotenv
load_dotenv()


# === 1. 実行ログ設定 ===
import logging

logging.basicConfig(
    filename="report_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    """メッセージをログ出力"""
    print(message)
    logging.info(message)

def run_script(script_name):
    """個別スクリプトの実行とエラーハンドリング"""
    try:
        start = time.time()
        log(f"▶️ {script_name} 実行開始")
        subprocess.run(["python3", script_name], check=True)
        elapsed = round(time.time() - start, 2)
        log(f"✅ {script_name} 実行完了（{elapsed}秒）")
    except subprocess.CalledProcessError as e:
        log(f"❌ {script_name} 実行失敗：{e}")
        raise SystemExit("処理を中断しました。")


# === 2. 実行開始ログ ===
# === ログ区切りとヘッダー ===
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log("\n" + "="*40)
log(f"🧾 売上レポート自動実行開始：{now}")
log("="*40)

log(f"\n=== 売上レポート 自動実行開始：{now} ===")

# === 3. 各スクリプトを順に実行 ===
run_script("sales_total.py")
run_script("high_sales.py")
run_script("generate_index.py")

# === 4. 実行終了ログ ===
end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log("\n" + "="*40)
log(f"✅ 売上レポート自動実行終了：{end}")
log("="*40 + "\n")
from datetime import datetime

# ==== 実行ログを追記 ====
log_path = "report_log.txt"
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_path, "a", encoding="utf-8") as log:
    log.write(f"[{now}] 自動売上レポート生成完了\n")

# === 5. メール通知機能（絵文字なし・UTF-8完全対応） ===
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import os


sender = "issey.rickowens@gmail.com"
password = os.getenv("EMAIL_PASSWORD")
receiver = "issey.rickowens@gmail.com"


subject = "売上レポート自動生成完了"
body = f"レポートが正常に生成されました。\n完了時刻：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain", "utf-8"))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)

        # 添付ファイルリスト
        attachments = [
            "outputs/sales_chart.png",
            "outputs/top_sales_plot.html"
        ]

        for file_path in attachments:
            with open(file_path, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
            part["Content-Disposition"] = f'attachment; filename="{os.path.basename(file_path)}"'
            msg.attach(part)

        server.send_message(msg)
        print("✅ メール通知＋添付送信しました！")

except Exception as e:
    print("⚠️ メール送信に失敗しました：", str(e).encode('utf-8', errors='ignore').decode('utf-8'))
