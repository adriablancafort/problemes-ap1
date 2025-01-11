import yogi


def es_valida(paraula: str, hex: str) -> bool:

    long = len(paraula)

    if long < 3:
        return False

    if hex[0] not in paraula:
        return False

    for lletra in paraula:
        if lletra not in hex:
            return False

    return True


def tuti(paraula: str, hex: str) -> bool:

    for lletra in hex:
        if lletra not in paraula:
            return False
        
    return True


def contar_punts(paraula: str) -> int:
    
    long = len(paraula)

    if long < 3:
        return 0
    elif long == 3:
        return 1
    elif long == 4:
        return 2
    else:
        return long


def main() -> None:

    hex = yogi.read(str)
    paraules: list[str] = []

    for paraula in yogi.tokens(str):
        paraules.append(paraula)
    
    contador = 0
    paraules = sorted(paraules)

    for paraula in paraules:
        if es_valida(paraula, hex):
            contador += contar_punts(paraula)
            print(paraula)
            if tuti(paraula, hex):
                contador += 10

    print("-----")
    print(contador)      

    
if __name__ == "__main__":
    main()