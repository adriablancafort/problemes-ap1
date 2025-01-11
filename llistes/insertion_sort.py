def insertion_sort(v: list[float]) -> None:
    """Ordena la llista v en ordre creixent."""

    n = len(v)
    for i in range(1, n):
        x = v[i]
        j = i
        while j > 0 and v[j - 1] > x:
            v[j] = v[j - 1]
            j -= 1
        v[j] = x