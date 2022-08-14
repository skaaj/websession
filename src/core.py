import json
import glob
from typing import Optional

def load_session(name: str) -> dict:
    path = _find_session_path(name)
    raw_session = _load_json(path)
    
    return raw_session

def _load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

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
