import logging
from logging import handlers
import os
from datetime import datetime

# ログフォルダ作成
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# ログファイル名（日付ごとに作成）
log_file = os.path.join(LOG_DIR, f"report_{datetime.now().strftime('%Y-%m-%d')}.log")

def setup_logger():
    logger = logging.getLogger("auto_report")
    logger.setLevel(logging.INFO)

    # すでにハンドラが付いている場合は重複防止
    if logger.handlers:
        return logger

    # ① フォーマット（プロ仕様）
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # ② コンソール出力（標準出力）
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # ③ ファイル出力（毎日1ファイル）
    file_handler = handlers.TimedRotatingFileHandler(
        log_file, when="midnight", backupCount=7, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
