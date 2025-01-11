import yogi

for i in yogi.tokens(str):
    n = len(i)
    for j in range(n):
        index = n - j - 1
        if index == 0:
            print(i[index])
        else:
            print(i[index], end="")