import yogi

t = yogi.read(int)

if t > 30:
    print("it's hot")
elif t < 10:
    print("it's cold")
else:
    print("it's ok")

if t >= 100:
    print('water would boil')

if t <= 0:
    print('water would freeze')