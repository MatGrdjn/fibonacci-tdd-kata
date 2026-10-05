# src/fizzbuzz_kata/cli.py
"""Command-line interface for fizzbuzz_kata."""

import argparse

from fibonacci_kata import fibonacci


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fibonacci-kata",
        description="Print the fibonacci term value for one number.",
    )

    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        help="The index of the fibonnaci sequence term you want to calculate.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.n is not None:
        print(f"{fibonacci(args.n):_}".replace("_", " "))
    else:
        parser.error("Provide an integer n.")


if __name__ == "__main__":
    main()
