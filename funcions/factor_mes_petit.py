def factor_mes_petit(n: int):

    i = 2

    while i*i < n:
        if n % i == 0:
            return i
        i += 1
        
    if i*i == n:
        return i
    
    return None
