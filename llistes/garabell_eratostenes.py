def eratostenes(m: int) -> list[bool]:
    """Retorna una llista de m+1 booleans tal que el valor a la posició i indica si i és o no és primer. Prec: m >= 2."""

    garbell = [False, False] + [True] * (m - 1)
    i = 2
    while i * i <= m:
        if garbell[i]:
            for j in range(2 * i, m + 1, i):
                garbell[j] = False
        i += 1
    return garbell

