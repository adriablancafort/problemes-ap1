def is_increasing(x: int) -> bool:
    if x < 10:
        return True
    if x % 10 > (x // 10) % 10:
        return is_increasing(x // 10)
    return False

print(is_increasing(1245789))
print(is_increasing(98))