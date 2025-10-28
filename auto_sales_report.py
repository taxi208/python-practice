# === auto_sales_report.py ===
import subprocess
import datetime
import os
import time

# === 1. 実行ログ設定 ===
log_file = "report_log.txt"

def log(message):
    """メッセージをログとコンソールに出力"""
    print(message)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{message}\n")

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
