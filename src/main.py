#!/usr/bin/env python3

import argparse
from start import start
from create import create
from config import config

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Web browser session launcher"
    )
    subparsers = parser.add_subparsers(
        title="commands",
        required=True
    )
    # websession start <name>
    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("--from-name", required=False, dest="name", metavar=("SESSION_NAME"))
    start_parser.add_argument("--from-bookmarks", required=False, nargs=2, dest="bookmarks", metavar=("PROFILE_PATH", "BOOKMARKS_PATH"))
    start_parser.add_argument("--force-new", required=False, action="store_true")
    start_parser.set_defaults(func=start)
    # websession create
    create_parser = subparsers.add_parser("create")
    create_parser.set_defaults(func=create)
    # websession config
    config_parser = subparsers.add_parser("config")
    config_parser.add_argument("--get", required=False, nargs=2, dest="get_query", metavar=("GROUP", "KEY"))
    config_parser.add_argument("--set", required=False, nargs=2, dest="set_query", metavar=("GROUP", "KEY_ASSIGN"))
    config_parser.set_defaults(func=config)
    return parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
