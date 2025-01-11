def selsort(v: list[float]) -> None:
    """
    Ordena una llista de nombres.
    """
    n = len(v)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if v[j] < v[min_index]:
                min_index = j

        v[i], v[min_index] = v[min_index], v[i]