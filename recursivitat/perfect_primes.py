def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def digit_sum(n: int) -> int:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def is_perfect_prime(n: int) -> bool:
    while True:
        if not is_prime(n):
            return False
        if n < 10:
            return True
        n = digit_sum(n)