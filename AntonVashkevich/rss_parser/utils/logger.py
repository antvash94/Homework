import logging
import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.info(f"{func.__name__}:start witn params:{args},{kwargs}")
            res = func(*args, **kwargs)
        except Exception as ex:
            logging.error(f"{ex.__str__()}")
            return 'Exception occurred \n' \
                   'try run with "--verbose"'
        else:
            logging.info(f"{func.__name__}:complete")
            return res
    return wrapper
