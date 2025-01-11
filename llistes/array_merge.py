def merge(v1: list[float], v2: list[float]) -> list[float]:
    """Retorna una llista L amb els elements de les llistes ordenades v1 i v2, ordenats."""

    L: list[float] = []
    i1 = 0
    i2 = 0

    while i1 < len(v1) and i2 < len(v2):
        if v1[i1] < v2[i2]:
            L.append(v1[i1])
            i1 += 1
        else:
            L.append(v2[i2])
            i2 += 1

    L.extend(v1[i1:])
    L.extend(v2[i2:])

    return L
