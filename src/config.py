def config(args) -> None:
    if not args.get_query and not args.set_query:
        raise AttributeError(f"--get or --set needs to be defined")
    elif args.get_query and args.set_query:
        raise AttributeError(f"--get or --set cannot be used at the same time")
    elif args.get_query:
        group, key = args.get_query
        _get(group, key)
    else:
        group, assign = args.set_query
        if "=" in assign:
            _set(group, assign)
        else:
            raise AttributeError(f"--set assignation malformed")

def _get(group, key):
    raise NotImplementedError()

def _set(group, assign):
    raise NotImplementedError()
