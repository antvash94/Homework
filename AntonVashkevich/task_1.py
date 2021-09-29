
class ContextManager:
    def __init__(self, file_path, mode="r"):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file:
            self.file.close()
        print(f"__exit__{(exc_type, exc_value, exc_tb)}")


with ContextManager("task_2.py") as file:
    print(file.readlines())
    #file.append()
    #file+1

