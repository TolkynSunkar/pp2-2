from __future__ import annotations

import math
import random


def main():
    print("=== 1) Built-in math functions ===")
    nums = [3, -7, 12, 0, 5]
    print("nums:", nums)
    print("min:", min(nums))
    print("max:", max(nums))
    print("abs(-7):", abs(-7))
    print("round(3.14159, 2):", round(3.14159, 2))
    print("pow(2, 10):", pow(2, 10))
    print()

    print("=== 2) math module ===")
    print("sqrt(81):", math.sqrt(81))
    print("ceil(3.2):", math.ceil(3.2))
    print("floor(3.9):", math.floor(3.9))
    print("sin(pi/2):", math.sin(math.pi / 2))
    print("cos(0):", math.cos(0))
    print("pi:", math.pi)
    print("e:", math.e)
    print()

    print("=== 3) random module ===")
    random.seed(42)  # for stable results in tests
    print("random():", random.random())
    print("randint(1, 10):", random.randint(1, 10))

    items = ["apple", "banana", "orange", "kiwi"]
    print("choice(items):", random.choice(items))

    deck = list(range(1, 11))
    random.shuffle(deck)
    print("shuffled deck:", deck)
    print()


if __name__ == "__main__":
    main()