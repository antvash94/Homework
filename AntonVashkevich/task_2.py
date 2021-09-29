from contextlib import contextmanager


@contextmanager
def context_manager(file_path, mode="r"):
    try:
        _file = open(file_path, mode)
        yield open(file_path, mode)
    except Exception as ex:
        print(f"__exit__{(ex.__class__, ex.__doc__)}")
    else:
        _file.close()


with context_manager("task_2.py") as f:
    print(f.readlines())
    # type error
    #f+1
    # attribute error
    f.append()

