from yogi import read

def avalua() -> bool:
    """
    Evalua Retorna el resultat d'evaluar una expressió llegida de l'entrada.
    """

    primer = read(str)

    if primer.isdigit():
        return int(primer)
    
    assert primer == "("

    r1 = avalua()
    op = read(str)
    r2 = avalua()

    darrer = read(str)

    assert darrer == ")"

    if op == "+":
        return r1 + r2
    
    if op == "-":
        return r1 - r2
    
    if op == "*":
        return r1 * r2
    
    assert False

print(avalua())