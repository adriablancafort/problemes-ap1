from yogi import read

def generar_zeros_ones(n: int, l: list[bool], i: int) -> None:

    if i == n:
        escriure(l)
    else:
        l[i] = False
        generar_zeros_ones(n, l, i + 1)
        l[i] = True
        generar_zeros_ones(n, l, i + 1)


def escriure(l: int) -> None:

    print(' '.join([str(1 if i else 0) for i in l]))


def main() -> None:
    n = read(int)
    
    generar_zeros_ones(n, [False for _ in range(n)], 0)


if __name__ == "__main__":
    main()
