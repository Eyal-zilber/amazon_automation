import logging
import os


LOGS_DIR = "logs/logs"
LOG_FILE = os.path.join(LOGS_DIR, "amazon_automation.log")


os.makedirs(LOGS_DIR, exist_ok=True)


logger = logging.getLogger("amazon_automation")
logger.setLevel(logging.INFO)


file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)