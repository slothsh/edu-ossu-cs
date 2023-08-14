#!/usr/bin/env python3

"""
Simple game that mimics the Legend of Zelda - The Lost Woods level

Link: 
"""

import random
import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple game that emulates 'The Lost Woods' level from the Legend of Zelda.")
    parser.add_argument("direction", type=str, nargs=1,
                        help="which direction the user must move in.")
    args = parser.parse_args()

    # TODO


if __name__ == "__main__":
    main()
