import yogi

def convert_to_base(n, b):
    if n < b:
        return str(n)
    else:
        return convert_to_base(n // b, b) + str(n % b)


def main() -> None:
    b = yogi.read(int)

    seq: list[int] = []

    for i in yogi.tokens(int):
        seq.append(i)

    digits = [0] * b 

    for n in seq:
        j = convert_to_base(n, b)
        for k in j:
            digits[int(k)] += 1

    m = max(digits)
    i = digits.index(m)

    print(i, m)


if __name__ == "__main__":
    main()
