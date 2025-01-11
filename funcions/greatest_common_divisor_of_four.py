## Write a function that computes the greatest common divisor of four natural numbers a, b, c and d using the fast version of the Euclidean algorithm.

def gcd4(a: int, b: int, c: int, d: int) -> int:

    while b > 0:
        r1 = a % b
        a = b
        b = r1

    while d > 0:
        r2 = c % d
        c = d
        d = r2

    while c > 0:
        r3 = a % c
        a = c
        c = r3

    return a
