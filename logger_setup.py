import logging
from logging.handlers import RotatingFileHandler
import time

def get_logger(name="sales_app_logger"):
    """ロガー（ログ出力用）を作成する関数"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 1MB × 3世代ローテーション
    handler = RotatingFileHandler(
        "report_log.txt",
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger


def measure_time(func):
    """処理時間を測定するデコレータ"""
    def wrapper(*args, **kwargs):
        logger = get_logger()
        start = time.time()
        logger.info(f"▶ {func.__name__} 開始")

        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"❌ {func.__name__} でエラー: {e}")
            raise
        finally:
            duration = time.time() - start
            logger.info(f"⏱ {func.__name__} 完了（{duration:.2f}秒）")

    return wrapper
