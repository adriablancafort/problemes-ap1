def mergesort(v: list[float]) -> None:
    """Ordena la llista L."""

    ordena_per_fusio(v, 0, len(v) - 1)


def ordena_per_fusio(L: list[float], esq: int, dre: int) -> None:
    """Ordena L[esq..dre]."""

    if esq < dre:
        mig = (esq + dre) // 2
        ordena_per_fusio(L, esq, mig)
        ordena_per_fusio(L, mig + 1, dre)
        fusiona(L, esq, mig, dre)


def fusiona(L: list[int], esq: int, mig: int, dre: int) -> None:
    """Ordena L[esq..dre] sabent que L[esq..mig] i L[mig+1..dre] estan ordenats."""

    R = L[0:0]
    i, j = esq, mig + 1
    while i <= mig and j <= dre:
        if L[i] <= L[j]:
            R.append(L[i])
            i += 1
        else:
            R.append(L[j])
            j += 1
    R.extend(L[i:mig + 1])
    R.extend(L[j:dre + 1])
    L[esq:dre + 1] = R
