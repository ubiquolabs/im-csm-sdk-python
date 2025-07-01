import os

from loguru import logger

log_path = os.getenv('LOG_PATH', 'logs/im-csm-sdk-python.log')
log_level = os.getenv('LOG_LEVEL', 'DEBUG')
logger.add(
    log_path,
    level=log_level,
    rotation='00:00',
    retention='1 month',
    compression='gz',
)

logger.info(f'Logger configuration: {log_path=}, {log_level=}')
