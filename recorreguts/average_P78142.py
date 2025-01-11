from yogi import tokens

s = 0
c = 0

for i in tokens(float):
    s += i
    c += 1

average = s/c

print(f"{average:.2f}")
