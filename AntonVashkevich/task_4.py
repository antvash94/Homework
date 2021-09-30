from contextlib import contextmanager


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
    else:
        print("exception not occurred")


with ignored(ZeroDivisionError, ValueError):
    print(2/0)
    print(x)
