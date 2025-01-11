from yogi import read
from typing import TypeAlias

Matriu: TypeAlias = list[list[int]]


def llegir(n: int, m: int) -> Matriu:
    return [[read(int) for _ in range(m)] for _ in range(n)]


def zigzag(m, n, mat: Matriu) -> bool:
    last = float('-inf')

    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                c = mat[i][j]
                print(c)
                if c <= last:
                    return False
                last = c
        else:
            for j in range(n - 1, -1, -1):
                c = mat[i][j]
                print(c)
                if c <= last:
                    return False
                last = c

    return True


def main() -> None:
    count = 1
    n, m = read(int), read(int)

    while n is not None:
        mat = llegir(n, m)

        result = "yes" if zigzag(n, m, mat) else "no"
        print(f"matriu {count}: {result}")

        count += 1
        n, m = read(int), read(int)


if __name__ == "__main__":
    main()
