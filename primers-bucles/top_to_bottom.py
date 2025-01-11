import yogi

a = yogi.read(int)
b = yogi.read(int)

if a < b:
    a, b = b, a

i = a
while i >= b:
    print(i)
    i -= 1