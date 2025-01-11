import yogi

a = yogi.read(int)
b = yogi.read(int)
c = yogi.read(int)

if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c

print(max)