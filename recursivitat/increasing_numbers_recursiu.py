def is_increasing(n: int) -> bool:
    ant = 10
    while n > 0:
        current_digit = n % 10
        if current_digit > ant:
            return False
        ant = current_digit
        n //= 10
    return True