import yogi

n = yogi.read(int)
p = 2

while p*p <= n:
    if n % p == 0:
        n //= p
        print(p)
    else: 
        p += 1
        
if n >= 2:
    print(n)

