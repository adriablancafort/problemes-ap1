from collections import Counter
import yogi

def main() -> None:
    n = yogi.read(int)
    inp: list[int] = []

    for _ in range(n):
        i = yogi.read(int)
        inp.append(i)

    inp.sort()
    counts = Counter(inp)

    for key, value in counts.items():
        print(f"{key} : {value}")

if __name__ == "__main__":
    main()
