from yogi import read


def generar_combinacions(n: int, no_sortits: list[bool], L: list[int], i: int) -> None:
    if i == n:
        escriure(L)
    else:
        for mot in range(1, n + 1):
            if no_sortits[mot - 1]:
                L[i] = mot
                no_sortits[mot - 1] = False
                generar_combinacions(n, no_sortits, L, i + 1)
                no_sortits[mot - 1] = True


def escriure(l: list[int]) -> None:
    print('(' + ','.join([str(i) for i in l]) + ')')


def main() -> None:
    n = read(int)
    generar_combinacions(n, [True for _ in range(n)], [0 for _ in range(n)], 0)


if __name__ == "__main__":
    main()