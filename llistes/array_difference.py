def difference(v1: list[float], v2: list[float]) -> list[float]:
    """Retorna una llista L amb la diferència dels elements de les llistes ordenades v1 i v2"""

    L: list[float] = []
    i1 = 0
    i2 = 0

    while i1 < len(v1) and i2 < len(v2):
        if v1[i1] == v2[i2]:
            i1 += 1
            i2 += 1
        elif v1[i1] > v2[i2]:
            i2 += 1
        elif v1[i1] < v2[i2]:
            if L == []:
                L.append(v1[i1])
            elif v1[i1] != L[-1] and v1[i1] != v1[i1 - 1]:
                L.append(v1[i1])
            i1 += 1
        
    if i1 < len(v1):
        for i in v1[i1:]:
            if i != L[-1]:
                L.append(i)

    return L


# Example usage:
v1 = [1, 2, 2, 2, 3, 4, 5, 5, 6]
v2 = [1, 2, 6]
print(difference(v1, v2))
