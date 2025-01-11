from yogi import read


def generar_combinacions_rec(n: int, l: list[int], i: int, n1: int) -> None:
    """
    Escriu totes les combinacions amb n zeros i uns, que comencin amb l[:i], 
    amb |l| = n ≥ i ≥ 0, i on n1 és el nombre d'uns que cal posar en l[i:].
    """

    if n1 >= 0 and n1 <= n - i:
        if i == n:
            escriure(l)
        else:
            l[i] = 0
            generar_combinacions_rec(n, l, i + 1, n1)
            l[i] = 1
            generar_combinacions_rec(n, l, i + 1, n1 - 1)


def escriure(l: int) -> None:

    print(' '.join([str(1 if i else 0) for i in l]))


def main() -> None:
    n = read(int)
    k = read(int)

    generar_combinacions_rec(n, [0 for _ in range(n)], 0, k)


if __name__ == "__main__":
    main()
