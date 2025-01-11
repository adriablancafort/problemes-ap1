def scalar_product(u: list[float], v: list[float]) -> float:

    e = 0
    for i in range(len(u)):
        e += u[i] * v[i]
    return e

