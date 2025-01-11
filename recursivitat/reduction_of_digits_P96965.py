def sum_of_digits(x: int) -> int:
    if x < 10:
        return x
    else:
        n = x // 10
        m = x % 10
        return m + sum_of_digits(n)

def reduction_of_digits(x: int) -> int:
    while x >= 10:
        x = sum_of_digits(x)
    return x