import yogi

def reversed_word(word: str) -> None:
    n = len(word)
    for i in range(n):
        index = n - i - 1
        if index == 0:
            print(word[index])
        else:
            print(word[index], end="")

def reversed_seq(seq: list, n: int) -> None:
    for i in range(n):
        index = n - i - 1
        reversed_word(seq[index])

def main() -> None:
    
    seq: list[str] = []
    n = yogi.read(int)

    for i in range(n):
        i = yogi.read(str)
        seq.append(i)

    reversed_seq(seq, n)

if __name__ == "__main__":
    main()