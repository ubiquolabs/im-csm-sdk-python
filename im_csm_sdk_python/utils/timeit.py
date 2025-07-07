import time
from datetime import timedelta
from functools import wraps

from humanize import precisedelta
from loguru import logger


def timeit(func):  # noqa: D103
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        human_time = precisedelta(timedelta(seconds=total_time))
        logger.debug(f'Function {func.__name__} Took {human_time}')
        return result

    return timeit_wrapper
