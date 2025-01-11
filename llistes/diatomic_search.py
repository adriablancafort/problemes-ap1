def position(x: float, v: list[float], left: int, right: int) -> int:
    """
    Funció que retorna la postició del caracter x en el vector v.
    """

    if left > right:
        return -1

    mid = (left + right) // 2

    if v[mid] == x:
        return mid
    elif v[mid] > x:
        return position(x, v, left, mid - 1)
    else:
        return position(x, v, mid + 1, right)