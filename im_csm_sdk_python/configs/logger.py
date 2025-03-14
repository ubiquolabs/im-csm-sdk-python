from loguru import logger

logger.add(
    "logs/im-csm-sdk-python.log",
    level="DEBUG",
    rotation="00:00",
    retention="1 month",
    compression="gz",
)
