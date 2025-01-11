from yogi import read, tokens
from typing import TypeAlias

Quadrat: TypeAlias = list[list[int]]


def bons_valors(q: Quadrat) -> bool:
    n = len(q)
    # comprovar que tots els valors són entre 1 i n²
    for i in range(n):
        for j in range(n):
            if not 1 <= q[i][j] <= n*n:
                return False
    # comprovar que no hi ha elements repetits
    vistos = [False for i in range(n * n + 1)]
    for i in range(n):
        for j in range(n):
            # ja se sap que 1 <= x <= n*n. per tant els accessos següents no són fora del vector
            x = q[i][j]
            if vistos[x]:
                return False
            vistos[x] = True
    # en aquest punt, ha passat totes les comprovacions
    return True


def sumes_iguals(q: Quadrat) -> bool:
    n = len(q)
    # trobar suma primera diagonal
    suma = sum([q[i][i] for i in range(n)])
    # comprovar suma segona diagonal
    if suma != sum([q[n - i - 1][i] for i in range(n)]):
        return False
    # comprovar sumes de cada fila i
    for i in range(n):
        if suma != sum(q[i]):
            return False
    # comprovar sumes de cada columna j
    for j in range(n):
        if suma != sum([q[i][j] for i in range(n)]):
            return False
    # en aquest punt, ha passat totes les comprovacions
    return True


def es_quadrat_magic(q: Quadrat) -> bool:
    """Indica si q és un quadrat màgic o no."""

    return bons_valors(q) and sumes_iguals(q)


def main() -> None:
    for n in tokens(int):
        q = [[read(int) for _ in range(n)] for _ in range(n)]
        print('yes' if es_quadrat_magic(q) else 'no')


if __name__ == "__main__":
    main()
