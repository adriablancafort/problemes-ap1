def is_leap_year(a: int) -> bool:
    return (a % 4 == 0 and a % 100 != 0) or (a % 100 == 0 and (a / 100) % 4 == 0)