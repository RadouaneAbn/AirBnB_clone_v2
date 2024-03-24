#!/usr/bin/python3
""" This script contains a function that
"""
from fabric.api import *
import os
import time


def do_pack():
    """ This script generates a .tgz archive from contents of the
        web_static folder
    """
    if not os.path.exists("versions"):
        os.mkdir("versions")
    archive = "versions/web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S"))
    try:
        local("tar -cvzf {} web_static".format(archive))
        return archive
    except Exception:
        return None
