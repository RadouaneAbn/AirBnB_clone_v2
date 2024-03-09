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

    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(releases_path))
    run("tar -zxf /tmp/{}.tgz -C {}".format(file_name, releases_path))
    # run(f"sudo rm /tmp/{file_name}.tgz")
    run("sudo mv {}/web_static/* {}".format(releases_path, releases_path))
    # run("rsync -a {}/web_static/* {}".format(releases_path, releases_path))
    run("rm -r {}/web_static/".format(releases_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {}/ /data/web_static/current".format(releases_path))
    print("New version deployed!")
    return True
