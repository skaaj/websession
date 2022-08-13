#!/usr/bin/env python3

import argparse

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Firefox session manager"
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

def start(args) -> None:
    name = args.name
    raise NotImplemented()

def create(args) -> None:
    raise NotImplemented()

def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
