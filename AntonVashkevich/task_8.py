def get_pairs(lst):
    """Returns a list of tuples containing pairs of elements."""
    if len(lst) > 1:
        result = list(zip(lst[:], lst[1:]))
        return result
    return None
