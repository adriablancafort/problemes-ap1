import yogi

a = yogi.read(int)
b = yogi.read(int)

if a > b:
    print("")
else:
    for i in range(a, b+1):
        if b == i:
            print(i)
        else:
            print(i, end=",")


