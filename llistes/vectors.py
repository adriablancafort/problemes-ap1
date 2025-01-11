def suma(v1: list[float], v2: list[float]) -> list[float]:

    v: list[float] = []
    for i in range(len(v1)):
        v.append(v1[i] + v2[i])
    return v

def producte_escalar(v1: list[float], v2: list[float]) -> list[float]:

    v: list[float] = []
    for i in range(len(v1)):
        v.append(v1[i] * v2[i])
    return v

def modul(v: list[float]) -> int:

    m = 0
    for x in range(len(v)):
        m += v[x] * v[x]
    return m

def cap_i_cua(v: list[float]) -> bool:
    return v == list(reversed(v))

def cap_i_cua_fast(v: list[float]) -> bool:
    l = len(v)
    for i in range(len(v)//2):
        if v[i] != v[l - i - 1]:
            return False
    return True

v1 = [1,2,3,4,6,5,4,3,2,1]
v2 = [4,25,3,4,5,6,7]

print(cap_i_cua_fast(v1))