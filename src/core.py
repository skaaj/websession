import os
import json
import glob
from typing import Optional

def load_session(name: str) -> dict:
    path = _find_session_path(name)
    raw_session = _load_json(path)
    return raw_session

def write_session(session: dict, scope: str) -> None:
    name = session["name"]
    obj = [{"url": it} for it in session["urls"]]
    path = f"./data/{scope}/{name}.json"
    _dump_json(obj, path)

def session_exists(name: str, scope: str) -> bool:
    return glob.glob(f"./data/user/{name}.json")

def _load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def _dump_json(obj: dict, path: str) -> None:
    os.makedirs("/".join(path.split("/")[:-1]), exist_ok=True)
    with open(path, "w+") as f:
        json.dump(obj, f, indent=4)

def _find_session_path(name: str) -> Optional[str]:
    filename = f"{name}.json"
    paths = [
        it for it in glob.glob(f"./data/**/*.json", recursive=True)
        if it.endswith(filename)
    ]
    if len(paths) > 0:
        return paths[0]
    else:
        raise RuntimeError("session path could not be found")
