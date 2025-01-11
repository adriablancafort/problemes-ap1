import yogi

h = yogi.read(int)
m = yogi.read(int)
s = yogi.read(int)

s += 1

if s >= 60:
    s = 0
    m += 1
    if m >= 60:
        m = 0
        h += 1
        if h >= 24:
            h = 0

print(f'{h:02d}:{m:02d}:{s:02d}')