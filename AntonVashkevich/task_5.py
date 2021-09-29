class WrongValue(Exception):
    pass


class NotAnInteger(WrongValue):
    pass


class NotEven(WrongValue):
    pass


class LessThan(WrongValue):
    pass


def check_number(number):

    if not number.isdigit():
        raise NotAnInteger("value must be an integer")
    elif int(number) < 3:
        raise LessThan("value must be greater than 3")
    elif int(number) % 2 != 0:
        raise NotEven("value must be even")
    return number




