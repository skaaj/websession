import sqlite3
from functools import partial

def get_session_from_bookmarks(profile_path, bookmarks_path):
    splitted_path = bookmarks_path.split("/")
    perform_on_profile = partial(_perform_on_db, f"{profile_path}/places.sqlite")
    folder_id = _get_folder_id(perform_on_profile, splitted_path)
    urls = _get_urls(perform_on_profile, folder_id)
    return {
        "name": splitted_path[-1],
        "urls": urls
    }

def _get_folder_id(perform_on_profile, splitted_path) -> int:
    def iter(cursor, remaining_path, current_parent) -> int:
        if remaining_path:
            # TODO: externalize query
            result = cursor.execute(
                f"""
                    select id
                    from moz_bookmarks
                    where
                        lower(title) = '{remaining_path[0]}' AND
                        parent = {current_parent}
                """
            ).fetchone()
            # TODO: handle no result case
            return iter(cursor, remaining_path[1:], result[0])
        else:
            return current_parent

    return perform_on_profile(
        lambda cursor: iter(cursor, splitted_path, 1)
    )

def _get_urls(perform_on_profile, parent):
    def root(cursor):
        # TODO: externalize query
        return cursor.execute(
            f"""
                select moz_places.url
                from moz_bookmarks
                left outer join moz_places
                on moz_places.id = moz_bookmarks.fk
                where
                    moz_bookmarks.parent = {parent}
            """
        ).fetchall()
        # TODO: handle no result case
    return [it[0] for it in perform_on_profile(root)]

def _perform_on_db(db_path, action):
    conn = sqlite3.connect(db_path)
    # TODO: handle locks and other failures
    try:
        cursor = conn.cursor()
        result = action(cursor)
        return result
    finally:
        conn.close()
