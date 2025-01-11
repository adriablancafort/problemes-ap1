def number_of_digits(n: int) -> int:

    i = abs(n)
    d = 0
    if i == 0:
        d = 1
    else:
        while i > 0:
            d += 1
            i //= 10

    return d
