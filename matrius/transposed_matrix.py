def transpose(m: list[list[int]]) -> None:
    mc = m[:][:]
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[j][i] = mc[i][j]

# Exemple
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m)
transpose(m)
print(m)