from yogi import tokens

def sieve_of_erathostenes(max_value: int) -> list[int]:
    """Funtion that uses sieve of erathostenes to generate a list with all the compound numbers till a certain max value"""
    sieve = [False, False] + [True] * (max_value + 1)
    prime = 3
    compound_number = 4 
    while compound_number <= max_value: #Cas concret del 2 per separat ja que així s'optimitza el programa
        sieve[compound_number] = False
        compound_number += 2
    while prime * prime <= max_value:
        if sieve[prime]:
            compound_number = prime * prime
            while compound_number <= max_value: 
                sieve[compound_number] = False
                compound_number += prime
        prime += 2 
    return sieve

def main() -> None:
    max_value = 10**6
    sieve = sieve_of_erathostenes(max_value)
    for number in tokens(int):
        if sieve[number]:
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")

if __name__ == "__main__":
    main()