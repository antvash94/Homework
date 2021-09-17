def generate_squares(num):
    """Function that takes a number as an argument and returns a dictionary,
     where the key is a number and the value is the square of that number."""
    result = {i: i**2 for i in range(1, num+1)}
    return result
