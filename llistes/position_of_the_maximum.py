def position_maximum(v: list[float], m: int) -> int:
    max_val = v[0]
    pos = 0

    for i in range(1, m):
        if v[i] >= max_val:
            max_val = v[i]
            pos = i

    return pos
