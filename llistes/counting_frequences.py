import yogi

def main() -> None:

    n = yogi.read(int)

    for _ in range(n):

        inp: list[int] = []

        for _ in range(n):
            i = yogi.read(str)
            inp.append(i)

        inp = sorted(inp)
        seq: list[int] = []
        count: list[int] = []

        for i in inp:
            if i in seq:
                index = seq.index(i)
                count[index] += 1
            else:
                seq.append(i)
                count.append(1)

        for i in range(len(seq)):
            print(f"{seq[i]} : {count[i]}")

if __name__ == "__main__":
    main()