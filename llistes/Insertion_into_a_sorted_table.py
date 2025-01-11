def insert(v: list[float]) -> None:
    i = 0
    while i < len(v) - 1 and v[i] < v[-1]:
        i += 1
    v.insert(i, v[-1])
    del v[-1]