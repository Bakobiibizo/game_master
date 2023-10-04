import json
import loguru
from pathlib import Path


def get_logger():
    logger = loguru.logger
    configuration = Path("helpers/logger.config.json").read_text(encoding="utf-8")

    config = json.loads(configuration)
    logger.add(**config)
    logger.info("logger setup")
    return logger