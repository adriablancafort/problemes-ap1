def print_matrix_in_order(matrix):
    if not matrix:
        print("Empty matrix")
        return

    n = len(matrix)
    m = len(matrix[0])

    for j in range(m):
        if j % 2 == 0:  # If column index is even, print top-down
            for i in range(n):
                print(matrix[i][j], end=" ")
        else:  # If column index is odd, print bottom-up
            for i in range(n - 1, -1, -1):
                print(matrix[i][j], end=" ")


# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print_matrix_in_order(matrix)
