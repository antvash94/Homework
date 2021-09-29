from contextlib import contextmanager


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
    else:
        print("exception not occurred")


with ignored(ZeroDivisionError):
    print(2/0)
