from yogi import read
from typing import TypeAlias

Quadrat: TypeAlias = list[list[int]]


def llegir(n: int) -> Quadrat:
    return [[read(int) for _ in range(n)] for _ in range(n)]


def check_aparicio(n: int, q: Quadrat) -> bool:
    nums = [False for _ in range(n * n)]

    for i in range(n):
        for j in range(n):
            num = q[i][j]
            if nums[num - 1]:
                return False
            nums[num - 1] = True

    return True


def check_rows(n: int, q: Quadrat) -> bool:
    row1 = sum(q[i][0] for i in range(n))

    for j in range(1, n):
        rown = sum(q[i][j] for i in range(n))
        if row1 != rown:
            return False

    return True


def check_columns(n: int, q: Quadrat) -> bool:
    col1 = sum(q[0][j] for j in range(n))

    for i in range(1, n):
        coln = sum(q[i][j] for j in range(n))
        if col1 != coln:
            return False

    return True


def check_diagonals(n: int, q: Quadrat) -> bool:
    diag1 = sum(q[i][i] for i in range(n))
    diag2 = sum(q[i][n - i - 1] for i in range(n))

    return diag1 == diag2


def main() -> None:
    n = read(int)

    while n is not None:
        q = llegir(n)

        if (
            check_aparicio(n, q)
            and check_rows(n, q)
            and check_columns(n, q)
            and check_diagonals(n, q)
        ):
            print("yes")
        else:
            print("no")

        n = read(int)


if __name__ == "__main__":
    main()
