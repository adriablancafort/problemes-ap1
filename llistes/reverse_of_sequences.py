import yogi

n = yogi.read(int)

while n is not None:

    seq: list[int] = []

    for _ in range(n):
        i = yogi.read(int)
        seq.append(i)

    for i in range(n):
        index = n - i - 1

        if index == 0:
            print(seq[index])
        else:
            print(seq[index], end=" ")

    if n == 0:
        print()

    n = yogi.scan(int)
