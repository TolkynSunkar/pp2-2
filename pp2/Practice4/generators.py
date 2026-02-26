from __future__ import annotations


class Countdown:
    """
    Custom iterator that counts down from start to 0.
    Example: for x in Countdown(3): -> 3,2,1,0
    """

    def __init__(self, start: int):
        if start < 0:
            raise ValueError("start must be >= 0")
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def fibonacci(n: int):
    """Generator: yield first n Fibonacci numbers."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def even_numbers(limit: int):
    """Generator: yield even numbers from 0 to limit (inclusive)."""
    if limit < 0:
        raise ValueError("limit must be >= 0")
    for x in range(0, limit + 1, 2):
        yield x


def read_lines(filepath: str):
    """Generator: yield lines from a file one by one (memory-friendly)."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


def main():
    print("=== 1) Iterator example (Countdown) ===")
    for x in Countdown(5):
        print(x, end=" ")
    print("\n")

    print("=== 2) Generator function (Fibonacci) ===")
    print(list(fibonacci(10)))
    print()

    print("=== 3) Another generator (even numbers) ===")
    print(list(even_numbers(20)))
    print()

    print("=== 4) Generator expression ===")
    squares = (i * i for i in range(1, 11))
    print(list(squares))
    print()


if __name__ == "__main__":
    main()