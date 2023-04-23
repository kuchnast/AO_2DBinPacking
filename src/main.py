import argparse
from typing import Optional, Sequence
from turtle import *

__version__ = "1.0.0"


def main(parameters: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.set_defaults(action=run)
    parser.add_argument("-v", "--version", action="version", version=f"bin_packing_2d {__version__}")
    parser.add_argument(
        "-i", "--input", type=str, nargs="?", dest="input", default=None, required=True, help="Input file"
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str,
        nargs="?",
        dest="algorithm",
        default="All",
        help="Algorithm that will be executed or all if not set",
    )
    args = parser.parse_args(parameters)
    args.action(args)


def run(args):
    print(args.input)


if __name__ == "__main__":
    main()

    color('red', 'yellow')
    begin_fill()
    forward(100)
    left(200)
    forward(100)
    left(200)
    end_fill()
    done()
