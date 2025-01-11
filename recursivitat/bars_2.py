from yogi import read

def bars(n: int):
    if n == 1:
        return "*"
    return n*"*" + "\n" + bars(n-1) + "\n" + bars(n-1)

n = read(int)

print(bars(n))