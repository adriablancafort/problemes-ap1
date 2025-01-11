from yogi import read
from typing import TypeAlias

Matriu: TypeAlias = list[list[int]]


def llegir_matriu(n: int, m: int) -> Matriu:
    Matriu = [[read(int) for _ in range(m)] for _ in range(n)]
    return Matriu


def row(Matriu: Matriu, i: int) -> None:
    row = Matriu[i - 1][:]
    print(f"row {i}:", end="")
    for r in row:
        print("", end=" ")
        print(r, end="")
    print("")


def column(Matriu: Matriu, j: int) -> None:
    print(f"column {j}:", end="")
    for i in range(len(Matriu)):
        c = Matriu[i][j - 1]
        print("", end=" ")
        print(c, end="")
    print("")


def element(Matriu: Matriu, i: int, j: int) -> None:
    element = Matriu[i - 1][j - 1]
    print(f"element {i} {j}: {element}")


def main() -> None:
    n, m = read(int), read(int)

    Matriu = llegir_matriu(n, m)

    d = read(str)

    while d is not None:
        if d == "row":
            i = read(int)
            row(Matriu, i)
        elif d == "column":
            j = read(int)
            column(Matriu, j)
        elif d == "element":
            i, j = read(int), read(int)
            element(Matriu, i, j)

        d = read(str)


if __name__ == "__main__":
    main()
