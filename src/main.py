#!/usr/bin/env python3

import argparse
from start import start
from create import create

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Firefox session launcher"
    )
    subparsers = parser.add_subparsers(
        title="commands",
        required=True
    )
    # ffsession start <name>
    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("name", help="name of the session")
    start_parser.set_defaults(func=start)
    # ffsession create
    create_parser = subparsers.add_parser("create")
    create_parser.set_defaults(func=create)
    return parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
