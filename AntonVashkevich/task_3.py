import time
import functools


def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open("log_file.txt", "a") as file:
            start = time.perf_counter()
            result = func(*args, **kwargs)
            time_elapsed = time.perf_counter() - start
            file.write(f"Function: {func.__name__}, Time: {time_elapsed}\n")
        return result

    return wrapper

