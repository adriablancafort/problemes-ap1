def sum(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """ Retorna la suma de a i b. """

    m = len(a)
    n = len(a[0])

    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(m)]
