#4.1

a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)
    return inner_function()


enclosing_funcion()

#4.2


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a
        print(a)
    return inner_function()


enclosing_funcion()

#4.3


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a
        print(a)
    return inner_function()

enclosing_funcion()
