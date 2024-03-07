#!/usr/bin/python3
""" This script contains a function that
"""
from fabric.api import *
import os
from datetime import datetime
import re

env.hosts = ['52.3.252.27', '54.160.117.45']
env.user = "ubuntu"


def do_pack():
    """ This function generates a .tgz archive from contents of the
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


def do_deploy(archive_path):
    """ This function destributes an archive to my web servers
    """
    if not os.path.exists(archive_path):
        return False

    file_name = re.search(r"([^\/]*)\..*$", archive_path)[1]
    releases_path = f"/data/web_static/releases/{file_name}"

    try:
        put(archive_path, "/tmp/")
        run(f"mkdir -p {releases_path}")
        run(f"tar -xzf /tmp/{file_name}.tgz -C {releases_path}")
        run(f"rm /tmp/{file_name}.tgz")
        run(f"mv -f {releases_path}/web_static/* {releases_path}")
        run(f"rm -rf {releases_path}/web_static")
        run(f"ln -sf {releases_path}/ /data/web_static/current")
        return True
    except Exception:
        return False
