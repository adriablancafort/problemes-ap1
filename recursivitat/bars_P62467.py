from yogi import read

def bars(n):
    if n == 1:
        return '*'
    else:
        ant = bars(n-1)
        return ant + '\n' + '*'*n + '\n' + ant

n = read(int)
print(bars(n))