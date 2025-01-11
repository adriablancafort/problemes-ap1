import yogi

a1 = yogi.read(int)
b1 = yogi.read(int)
a2 = yogi.read(int)
b2 = yogi.read(int)

if b1 < a2:
    print('[]')
elif b2 < a1:
    print('[]')
else:
    if a1 > a2:
        inf = a1
    else:
        inf = a2

    if b1 < b2:
        sup = b1
    else:
        sup = b2

    print(f'[{inf},{sup}]')