def get_longest_word(s: str) -> str:
    """Returns the longest word in the given string."""
    result = sorted(s.split(), key=lambda x: (len(x), -s.index(x)))[-1]
    return result
