"""
Connvention:
Let 0 -> heads
Let 1 -> tails
"""

import matplotlib.pyplot as plt
from random import randint
from rich import print


def flip(bias: float = 0.5) -> int:
    if bias <= 0 or bias >= 1:
        return -1
    return 1 if randint(0, 1) < bias else 0


def plot(x_coordinates: list[int], y_coordinates: list[float]):
    plt.plot(x_coordinates, y_coordinates, label="Experimental Values")
    plt.axhline(y=0.5, color='r', label="Expected Value")

    plt.xlabel("Total Flips")
    plt.ylabel("Proportion of Heads")
    plt.title("Coin Flips Demonstrating the Law of Large Numbers")

    plt.ylim(0, 1)

    plt.legend()

    plt.show()


def simulate_flips(amount_of_flips: int = 1000) -> tuple[list[float], list[int]]:
    # list of coordinates in the form of `(total number of flips, proportion of heads)`
    proportions: list[float] = []
    total_flips: list[int] = [i for i in range(1, amount_of_flips, 10)]

    for i in range(1, amount_of_flips, 10):
        flips = [flip() for _ in range(i)]

        proportions.append(flips.count(0) / len(flips))

    return proportions, total_flips


def main() -> None:
    proportions, total_flips = simulate_flips(10000)
    print(proportions)
    plot(total_flips, proportions)


if __name__ == "__main__":
    print(main())
