def call_once(func):
    result = None

    def wrapper(*args):
        nonlocal result
        if result is None:
            result = func(*args)
        return result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b
