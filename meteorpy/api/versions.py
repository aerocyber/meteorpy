# Copyright (c) 2022 aerocyber
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import json
import os
import requests


class UnfetchedVersions(Exception):
    ...


def fetchDB():
    try:
        db = requests.get("https://aerocyber.github.io/meteorpy/versions.json").json()
        f = open(
            os.path.join(
                os.path.join(
                    os.path.expanduser("~"),
                    ".meteorpy",
                    "Database.json"
                )
            )
        )
        json.dump(f, db)
        f.close()
        return db
    except Exception as e:
        raise UnfetchedVersions("The version cache is empty and versions couldn't be fetched from remote url.")


def versions():
    """Return a list of supported python versions.
    """
    db_cache = os.path.join(
        os.path.expanduser("~"),
        ".meteorpy",
        "Database.json"
    )
    if not os.path.exists(db_cache): # If meteorpy is run for the first time, the file will be empty.
        db_cache = fetchDB()
    
    if db_cache is not dict: # If meteorpy is not using the remote url, it will still be the path. Read it.
        _file = open(db_cache, 'r') # Forcing read for security purposes.
        db_cache = json.load(_file)
        _file.close()
