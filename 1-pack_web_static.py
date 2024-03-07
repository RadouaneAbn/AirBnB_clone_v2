#!/usr/bin/python3
""" This script contains a function that
"""
from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """ This script generates a .tgz archive from contents of the
        web_static folder
    """
    if not os.path.exists("versions"):
        os.mkdir("versions")
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"web_static_{current_time}.tgz"
    try:
        local(f"tar -cvzf versions/{file_name} web_static")
        return f"versions/{file_name}"
    except Exception:
        return None
