def is_palindromic(n: int) -> bool:
    i = str(n)
    return i == i[::-1]