def sum_divisors(n: int) -> int:

    s = 0
    i = 1

    if n == 1:
        return 1

    while i*i < n:
        if n % i == 0:
            s += i
            s += n // i
        i += 1

    if i*i == n:
        s += i

    return s