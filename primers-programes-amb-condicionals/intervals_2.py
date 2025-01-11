import yogi

a1 = yogi.read(int)
b1 = yogi.read(int)
a2 = yogi.read(int)
b2 = yogi.read(int)

if a1 == a2 and b1 == b2:
    print('=')
elif a1 >= a2 and b1 <= b2:
    print('1')
elif a2 >= a1 and b2 <= b1:
    print('2')
else:
    print('?')