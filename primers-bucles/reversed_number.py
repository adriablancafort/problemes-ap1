import yogi

n = yogi.read(int)

if n == 0:
    print(0, end="")

while n > 0:
    rem = n % 10
    print(rem, end="")
    n //= 10

print("")