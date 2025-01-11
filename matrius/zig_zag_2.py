from yogi import read
from typing import TypeAlias

Matriu: TypeAlias = [list[list[int]]]


def llegir(n, m) -> Matriu:
    return [[read(int) for _ in range(m)] for _ in range(n)]


def zigzag(q) -> bool:
    """Retorna true si els elements de la matriu en zig zag son estrictament creixents."""

    n = len(q)
    m = len(q[0])
    old = -9999

    for j in range(m):
        if j % 2 == 0:
            for i in range(n):
                new = q[i][j]
                if old >= new:
                    return False
                old = new
        else:
            for i in range(n - 1, -1, -1):
                new = q[i][j]
                if old >= new:
                    return False
                old = new

    return True


def main() -> None:

    n, m = read(int), read(int)
    c = 1

    while n is not None:
        q = llegir(n, m)
        print(f'matriu {c}:', end=" ")
        print('yes' if zigzag(q) else 'no')
        n, m = read(int), read(int)
        c += 1


if __name__ == "__main__":
    main()
