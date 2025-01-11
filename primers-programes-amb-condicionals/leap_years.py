import yogi

a = yogi.read(int)

if (a % 4 == 0 and a % 100 != 0) or (a % 100 == 0 and (a / 100) % 4 == 0):
    print("YES")
else:
    print("NO")

