import yogi

a1 = yogi.read(int)
b1 = yogi.read(int)
a2 = yogi.read(int)
b2 = yogi.read(int)

if b1 < a2:
    intersection = '[]'
elif b2 < a1:
    intersection = '[]'
else:
    if a1 > a2:
        inf = a1
    else:
        inf = a2

    if b1 < b2:
        sup = b1
    else:
        sup = b2

    intersection = f'[{inf},{sup}]'

if a1 == a2 and b1 == b2:
    equal = '='
elif a1 >= a2 and b1 <= b2:
    equal = '1'
elif a2 >= a1 and b2 <= b1:
    equal = '2'
else:
    equal = '?'

print(f"{equal} , {intersection}")
