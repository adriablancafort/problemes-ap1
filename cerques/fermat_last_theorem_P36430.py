from math import sqrt
from yogi import read

def fermat_last_theorem(a: int, b : int, c: int, d: int):
    for x in range(a,b+1):
        for y in range(c,d+1):
            z = sqrt(x*x + y*y)
            if z == int(z):
                return [x, y, int(z)]
    return [1, 1, None]

a, b, c, d = read(int), read(int), read(int), read(int)

[x, y, z] = fermat_last_theorem(a, b, c, d)

if z is not None:
    print(f'{x}^2 + {y}^2 = {z}^2')
else:
    print("No solution!")