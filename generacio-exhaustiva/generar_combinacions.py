def escriure(L: list[int]) -> None:
    """Escriu els elements de L en el format prescrit."""

    print(','.join([str(x) for x in L]))
    

def generar_combinacions(n: int) -> None:
    """Escriu totes les combinacions d'n zeros i uns, per a n ≥ 0."""

    generar_combinacions_rec(n, [-1 for _ in range(n)], 0)


def generar_combinacions_rec(n: int, L: list[int], i: int) -> None:
    """Escriu totes les combinacions d'n zeros i uns que comencin amb L[:i], amb |L| = n ≥ i ≥ 0."""

    if i == n:
        escriure(L)
    else:
        L[i] = 0
        generar_combinacions_rec(n, L, i + 1)
        L[i] = 1
        generar_combinacions_rec(n, L, i + 1)


generar_combinacions(5)