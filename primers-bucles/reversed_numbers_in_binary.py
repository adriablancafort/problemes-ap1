import yogi

n = yogi.read(int)

if n == 0:
    print(0, end="")

while n > 0:
    rem = n % 2
    print(rem, end="")
    n //= 2

print("")