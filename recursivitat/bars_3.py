from yogi import read

def bars(n: int):
    if n == 1:
        return "*"
    return bars(n-1) + "\n" + bars(n-1) + "\n" + n*"*"

n = read(int)

print(bars(n))