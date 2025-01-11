from yogi import read


def generar_combinacions(n: int, mots: list[str], L: list[str], i: int) -> None:
    if i == n:
        escriure(L)
    else:
        for mot in mots:
            if i == 0 or mot not in L[:i]:
                L[i] = mot
                generar_combinacions(n, mots, L, i + 1)


def escriure(L: list[str]) -> None:
    print('(' + ','.join(L) + ')')


def main() -> None:
    n = read(int)
    mots = [read(str) for _ in range(n)]
    generar_combinacions(n, mots, ['' for _ in range(n)], 0)


if __name__ == "__main__":
    main()
