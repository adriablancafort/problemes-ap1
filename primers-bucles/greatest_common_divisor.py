import yogi

a = yogi.read(int)
b = yogi.read(int)

n1 = a
n2 = b

while b > 0:
    r = a % b
    a = b
    b = r

print(f'The gcd of {n1} and {n2} is {a}.')