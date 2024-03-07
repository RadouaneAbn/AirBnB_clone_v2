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
    """
        Deploys and distributes an archive to web servers
    """

    if os.path.exists(archive_path):
        put(archive_path, "/tmp/")
        archive_file = archive_path[9:]
        server_archive = "/tmp/{}".format(archive_file)

        archive_base, ext = os.path.splitext(archive_file)
        new_path = "/data/web_static/releases/{}".format(archive_base)

        run("sudo mkdir -p {}".format(new_path))
        run("sudo tar -zxf {} -C {}".format(server_archive, new_path))
        run("sudo rm  {}".format(server_archive))
        run("sudo mv {}/web_static/* {}".format(new_path, new_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_path))

        print("New version deployed!")

        return True

    return False