def producte(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """
    Retorna el producte de A i B:
    """

    m = len(A)
    n = len(B)
    p = len(B[0])
    return [
        [
            sum([A[i][k] * B[k][j] for k in range(n)])
            for j in range(p)
        ]
        for i in range(m)
    ]