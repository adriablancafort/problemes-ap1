import yogi

s = yogi.read(int)

h = s // 3600
m = (s % 3600) // 60
s = s % 60

print(h, m, s)