import subprocess
from core import load_session

def start(args) -> None:
    print(args)
    name = args.name.lower()
    session = load_session(name)
    urls = [it["url"] for it in session]
    subprocess.run(["firefox", "-url"] + urls, capture_output=True)
