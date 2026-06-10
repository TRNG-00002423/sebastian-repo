import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file="test_framework.log", console_level=logging.INFO):
    logger = logging.getLogger("qa_framework")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,
        backupCount=3,
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - "
            "%(filename)s:%(lineno)d - %(message)s"
        )
    )

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
