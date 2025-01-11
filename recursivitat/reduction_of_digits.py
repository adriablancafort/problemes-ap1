
def sum_of_digits(x: int) -> int:
    if x < 10:
        return x
    return sum_of_digits(x // 10) + x % 10

def reduction_of_digits(x: int) -> int:
    m = sum_of_digits(x)
    if m < 10:
        return m
    return sum_of_digits(m)

print(reduction_of_digits(12345))
