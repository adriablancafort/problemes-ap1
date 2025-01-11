from dataclasses import dataclass
from typing import TypeAlias
from yogi import read


@dataclass
class Rectangle:
    amplada: int
    alçada: int


Rectangles: list[Rectangle] = []


def ordenar_rectangles(Rectangles):
    """Retorna els rectangles ordenats per area creixent."""

    return sorted(Rectangles, key=lambda r: (r.amplada * r.alçada, -2 * (r.amplada + r.alçada), r.amplada))


def main():
    num_rectangles = read(int)

    while num_rectangles is not None:

        for _ in range(num_rectangles):
            NouRect = Rectangle(read(int), read(int))
            Rectangles.append(NouRect)

        rectangles_ordenats = ordenar_rectangles(Rectangles)

        for rectangle in rectangles_ordenats:
            print(rectangle.amplada, rectangle.alçada)

        print("----------")

        Rectangles.clear()

        num_rectangles = read(int)


if __name__ == "__main__":
    main()
