from task_5 import check_number


def is_prime(number):
    return all(number % i for i in range(2, number))


def goldbach_resolve(num):
    for i in range(2, num):
        if is_prime(i):
            if is_prime(num-i):
                print(num, '=', i, '+', num-i)


while True:
    _i = input("Even integer greater than 3 or 'q' for exit:")
    if _i.lower() == "q":
        break
    else:
        number = int(check_number(_i))
        goldbach_resolve(number)


