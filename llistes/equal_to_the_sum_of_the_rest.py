import yogi


def is_equal_to_sum(seq: list[int]) -> bool:

    total_sum = sum(seq)

    for num in seq:
        if total_sum == 2*num:
            return True

    return False


def main() -> None:
    
    n = yogi.read(int)

    while n is not None:
        
        seq: list[int] = []

        for _ in range(n):
            i = yogi.read(int)
            seq.append(i)
        
        if is_equal_to_sum(seq):
            print("YES")
        else:
            print("NO")

        n = yogi.scan(int)


if __name__ == "__main__":
    main()