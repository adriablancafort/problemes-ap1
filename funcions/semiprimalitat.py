def semiprimalitat(n: int) -> [tuple[int, int]]:

    i = 2

    while i*i < n:
        if n % i == 0:
            
            return [a, n // a]
            a = i

    else:
        return None
