def remember_result(func):
    result = None

    def wrapper(*args):
        nonlocal result
        print(f"Last result = '{result}'")
        result = func(*args)
        return result
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result
