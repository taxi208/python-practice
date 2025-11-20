# === send_mail.py ===
# レポート添付メール送信スクリプト
# by issey / 2025 ポートフォリオ対応

import smtplib
import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv

# --- .env 読み込み ---
load_dotenv()

def send_report_via_email(attachments, sender, receiver):
    """売上レポートをメール添付して送信する"""

    password = os.getenv("EMAIL_PASSWORD")
    if not password:
        raise ValueError("⚠️ エラー：EMAIL_PASSWORD が .env に設定されていません")

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "📈 売上レポート自動生成完了通知"

    body = (
        "売上レポートが正常に生成されました。\n"
        f"完了時刻：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    msg.attach(MIMEText(body, "plain", "utf-8"))

    # 添付ファイル追加
    for file_path in attachments:
        with open(file_path, "rb") as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
            part["Content-Disposition"] = (
                f'attachment; filename="{os.path.basename(file_path)}"'
            )
            msg.attach(part)

    # Gmail 送信
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("📧 メール送信成功！")
    except Exception as e:
        print(f"⚠️ メール送信失敗: {e}")


if __name__ == "__main__":
    # 添付ファイル
    files = [
        "outputs/sales_chart.png",
        "outputs/top_sales_plot.html"
    ]

    send_report_via_email(
        attachments=files,
        sender="issey.rickowens@gmail.com",
        receiver="issey.rickowens@gmail.com"
    )
