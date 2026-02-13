import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path

PROJECT_LOGGER_NAME = "webtag"

def setup_logging():
    log_dir = Path("log")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(PROJECT_LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - (%(filename)s:%(lineno)d) '
        '- [%(levelname)s] - %(message)s',
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    debug_handler = RotatingFileHandler(
        log_dir / "debug.log",
        maxBytes=10_000_000, 
        backupCount=5,
    )
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    logger.addHandler(debug_handler)

    warning_handler = RotatingFileHandler(
        log_dir / "warning.log",
        maxBytes=10_000_000,
        backupCount=10,
    )
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)
    logger.addHandler(warning_handler)

    error_handler = RotatingFileHandler(
        log_dir / "error.log",
        maxBytes=10_000_000,
        backupCount=10,
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)


def get_logger(name: str) -> logging.Logger:
    if name == "__main__":
        return logging.getLogger(PROJECT_LOGGER_NAME)
    if name.startswith(PROJECT_LOGGER_NAME):
        return logging.getLogger(name)
    return logging.getLogger(f"{PROJECT_LOGGER_NAME}.{name}")