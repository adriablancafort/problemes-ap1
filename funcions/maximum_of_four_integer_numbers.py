def max4(a: int, b: int, c: int, d: int) -> int:
    if a >= b:
        if a >= c:
            if a >= d:
                return a
            else:
                return d
        elif a <= c:
            if c >= d:
                return c
            else:
                return d
    elif a <= b:   
        if b >= c:
            if b >= d:
                return b
            else:
                return d
        elif b <= c:
            if c >= d:
                return c
            else:
                return d
