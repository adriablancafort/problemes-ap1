from yogi import read

n = read(int)

a = []
c = 0

for i in range(n):
    m = read(int)
    a.append(m)

l = a[-1]

for i in a:
    if l == i:
        c += 1

if c == 0:
    print(c)
else:
    print(c-1)