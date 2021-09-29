from time import sleep


def endless_fib_generator():
    a, b = 0, 1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b


g = endless_fib_generator()

while True:
    print(f"{next(g)}", end=' ')
    sleep(0.1)
