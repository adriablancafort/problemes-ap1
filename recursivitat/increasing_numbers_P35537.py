def is_increasing(n: int, prev_digit: int = 10) -> bool:
    if n == 0:
        return True
    current_digit = n % 10
    if current_digit > prev_digit:
        return False
    return is_increasing(n // 10, current_digit)