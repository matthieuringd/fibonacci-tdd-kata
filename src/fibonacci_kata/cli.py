"""Command-line interface for fibonacci_kata."""

import argparse

from fibonacci_kata import fibonacci, fibonacci_mod


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fibonacci-kata",
        description="Compute Fibonacci values for one number or a range of numbers.",
    )

    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        help="A single Fibonacci index.",
    )

    parser.add_argument(
        "--start",
        type=int,
        help="Start of a range (inclusive).",
    )

    parser.add_argument(
        "--end",
        type=int,
        help="End of a range (inclusive).",
    )

    parser.add_argument(
        "--mod",
        type=int,
        help="Compute Fibonacci values modulo this number.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.start is not None and args.end is not None:
        for i in range(args.start, args.end + 1):
            if args.mod is not None:
                print(fibonacci_mod(i, args.mod))
            else:
                print(fibonacci(i))

    elif args.n is not None:
        if args.mod is not None:
            print(fibonacci_mod(args.n, args.mod))
        else:
            print(fibonacci(args.n))

    else:
        parser.error("Provide either a single number, or --start and --end.")


if __name__ == "__main__":
    main()
