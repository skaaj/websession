from core import write_session, session_exists

def create(args) -> None:
    name = _get_session_name()
    urls = _get_urls()
    if urls:
        _confirm_creation({
            "name": name,
            "urls": urls
        })

def _get_session_name() -> str:
    name = input("Session name: ")
    if session_exists(name, "user"):
        raise RuntimeError(f"{name} session already exists.")
    return name

def _get_urls() -> list:
    urls = []
    while True:
        url = input(f"URL {len(urls) + 1} (q to quit): ")
        if url.lower() != "q":
            urls.append(url)
        else:
            return urls

def _confirm_creation(session: dict) -> None:
    name = session["name"]
    urls = session["urls"]
    confirm = input(f"Confirm creation of {name} (size: {len(urls)}) ? (Y/n) ")
    if confirm.lower() != "n":
        write_session(session, "user")
        print(f"New session 'user/{name}.json' created.")
    else:
        print("Creation aborted. Bye!")
