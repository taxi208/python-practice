import logging
from logging import handlers
from datetime import datetime
import os

# ログフォルダ作成
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# ログファイル名（固定ファイル名 → ローテーション対応）
log_file = os.path.join(LOG_DIR, "auto_report.log")

def setup_logger():
    logger = logging.getLogger("auto_report")
    logger.setLevel(logging.INFO)

    # すでにハンドラが付いている場合は重複防止
    if logger.handlers:
        return logger

    # ---- フォーマット ----
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # ---- コンソール出力 ----
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # ---- ファイル出力（毎日ローテーション）----
    file_handler = handlers.TimedRotatingFileHandler(
        log_file, when="midnight", backupCount=7, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

