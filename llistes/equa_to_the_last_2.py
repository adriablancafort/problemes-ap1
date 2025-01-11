import yogi

def llegir_paraules() -> list[str]:
    paraules: list[str] = []
    primera = yogi.read(int)
    for paraula in yogi.tokens(int):
        paraules.append(paraula)
    return paraules

def ocurrencies(trobar: str, paraules: list[str]) -> int:
    c = 0
    for paraula in paraules:
        if paraula == trobar:
            c += 1
    return c

def main() -> None:
    paraules = llegir_paraules()
    if paraules == []:
        print(0)
    else:
        print(ocurrencies(paraules[-1], paraules) - 1)

if __name__ == '__main__':
    main()
