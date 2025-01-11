import yogi

def pica_destats(h: int) -> bool:

    p1, p2, p3 = yogi.read(int), yogi.read(int), yogi.read(int)

    while p3 != 0:      
        if p1 < p2 > p3 and p2 > h:
            return True
        p1, p2, p3 = p2, p3, yogi.read(int)
        
    return False

h = 3143

if pica_destats(h):
    print("YES")
else:
    print("NO")