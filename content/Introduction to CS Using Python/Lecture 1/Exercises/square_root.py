#!/usr/bin/env python3

"""
This implementation is based on Heron of Alexandria's algorithm for finding the
square root of a number.

Reference: https://en.wikipedia.org/wiki/Hero_of_Alexandria
"""

import random
import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple Square Root Calculator")
    parser.add_argument("number", type=int, nargs=1, help="number to find square root.")
    args = parser.parse_args()

    n = args.number[0]
    guess = random.randint(n, n + 1)

    while guess * guess - n > 0.00001:
        guess = (guess + n/guess) / 2

    print(guess)


if __name__ == "__main__":
    main()
