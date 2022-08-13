#!/usr/bin/env python3

import os
import json
import argparse
import subprocess
from typing import Optional

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

def start(args) -> None:
    name = args.name
    path = find_session_by_name(name)
    session = load_session(path)
    urls = [it["url"] for it in session]
    subprocess.run(["firefox", "-url"] + urls, capture_output=True)

def create(args) -> None:
    raise NotImplemented()

def find_session_by_name(name: str) -> Optional[str]:
    full_name = f"{name}.json"
    for p, d, f in os.walk('.'):
        for filename in f:
            if filename == full_name:
                return f"{p}/{filename}"

def load_session(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def load_browser() -> str:
    with open("./data/config.json", "r") as f:
        return json.load(f)["browser"]

def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
