import string


def is_palindrome(text: str) -> bool:
    """check whether a string is a palindrome or not."""
    check_string = ""
    for ch in text.lower().replace(" ", ""):
        if ch not in string.punctuation:
            check_string += ch
    if check_string == check_string[::-1]:
        return True
    return False
