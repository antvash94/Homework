def is_palindrome(string: str) -> bool:
    """check whether a string is a palindrome or not."""
    string = string.lower()
    if string == string[::-1]:
        return True
    return False
