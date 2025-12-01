import logging
from logging import handlers
import os
from datetime import datetime

def setup_logger():
    LOG_DIR = "logs"
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(LOG_DIR, "auto_report.log")

    # ロガー取得（型を明示）
    logger: logging.Logger = logging.getLogger("auto_report")
    logger.setLevel(logging.INFO)

    # 既存ハンドラがある場合はクリア（重複防止）
    if logger.hasHandlers():
        logger.handlers.clear()

    # 読みやすいログフォーマット
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )

    # コンソール出力
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # ファイル出力（1日ごとにローテーション）
    file_handler = handlers.TimedRotatingFileHandler(
        log_file, when="midnight", backupCount=7, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
