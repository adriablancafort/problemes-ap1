import yogi

n = yogi.read(int)

d = 1
i = abs(n)
while i >= 10:
    d += 1
    i //= 10

print(f'The number of digits of {n} is {d}.')