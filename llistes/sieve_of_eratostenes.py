import yogi
import math


def sieve_of_eratosthenes(max_value: int) -> list[int]:
    sieve = [False, False] + [True] * (max_value - 1)
    
    for compound_number in range(4, max_value + 1, 2):
        sieve[compound_number] = False

    prime = 3
    while prime * prime <= max_value:
        if sieve[prime]:
            for compound_number in range(prime * prime, max_value + 1, prime * 2):
                sieve[compound_number] = False
        prime += 2

    return sieve


def main() -> None:

    n = yogi.read(int)

    while n is not None:

        if n == 0:
            print(f"{n} is not prime")
        else:
            p = sieve_of_eratosthenes(n)

            if p[n]:
                print(f"{n} is prime")
            else:
                print(f"{n} is not prime")

        n = yogi.scan(int)


if __name__ == "__main__":
    main()