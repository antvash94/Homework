def get_digits(num):
    """Returns a tuple of a given integer's digits."""
    result = tuple(int(i) for i in str(num))
    return result
