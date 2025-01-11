def transpose(m: list[list[int]]) -> None:
    """Transposa la matriu quadrada M."""

    n = len(m)
    for i in range(n):  # per cada índex fila
        for j in range(i + 1, n):  # per cada columna per sota de la diagonal
            m[i][j], m[j][i] = m[j][i], m[i][j]