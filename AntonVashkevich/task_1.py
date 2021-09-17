def replace_quotes(sting: str) -> str:
    """Receives a string and replaces all " symbols with ' and vise versa."""
    result = ""
    for i in sting:
        if i == "\'":
            result += "\""
        elif i == "\"":
            result += "\'"
        else:
            result += i
    return result

