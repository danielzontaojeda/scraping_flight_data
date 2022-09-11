import logging
from datetime import date
from pathlib import Path


def create_directory():
    Path("./logs").mkdir(parents=True, exist_ok=True)


def get_logger(name):
    create_directory()

    logger = logging.getLogger(name)
    logging.basicConfig(level=logging.INFO)

    today = date.today().strftime("%Y-%m-%d")

    f_format = logging.Formatter(
        "%(levelname)s - %(name)s(%(funcName)s)  - %(message)s"
    )
    f_handler = logging.FileHandler(rf"logs\{today}.log")
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    return logger


if __name__ == "__main__":
    logger = get_logger(__name__)
    print(logger)
