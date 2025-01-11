from dataclasses import dataclass
from typing import List


@dataclass
class Rectangle:
    width: int
    height: int


def sort_rectangles(rectangles: List[Rectangle]) -> List[Rectangle]:
    # Sorting criteria: area (ascending), perimeter (descending), width (ascending)
    sorted_rectangles = sorted(rectangles, key=lambda r: (
        r.width * r.height, -(2 * r.width + 2 * r.height), r.width))
    return sorted_rectangles


def print_rectangles(rectangles: List[Rectangle]) -> None:
    for rectangle in rectangles:
        print(f"{rectangle.width} {rectangle.height}")


def main():
    # Read the number of rectangles
    num_rectangles = int(input())

    while num_rectangles > 0:
        # Read rectangle dimensions
        rectangles = [Rectangle(*map(int, input().split()))
                      for _ in range(num_rectangles)]

        # Sort rectangles
        sorted_rectangles = sort_rectangles(rectangles)

        # Print sorted rectangles
        print_rectangles(sorted_rectangles)

        # Print separator line
        print("----------")

        # Read the number of rectangles for the next case
        num_rectangles = int(input())


if __name__ == "__main__":
    main()
