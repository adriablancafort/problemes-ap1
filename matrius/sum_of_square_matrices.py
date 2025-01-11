def sum(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    c = [[(a[i][j] + b[i][j]) for i in range(len(a[0]))] for j in range(len(a[0]))]
    return c