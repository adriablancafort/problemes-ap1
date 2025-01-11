from typing import TypeAlias

Matrix: TypeAlias = list[list[int]]


def product(a: Matrix, b: Matrix) -> Matrix:

    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    return c

# Example
a = [[1, 2], [1, 2]]
b = [[1, 2], [1, 2]]

result = product(a, b)
print(result)
