import logging
import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"{func.__name__}:start ")
            res = func(*args, **kwargs)
        except Exception as ex:
            logging.error(f"{ex}: occurred")
            return ''
        else:
            logging.info(f"{func.__name__}:complete")
            return res
    return wrapper
