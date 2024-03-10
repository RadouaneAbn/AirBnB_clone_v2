#!/usr/bin/python3
""" This script contains a function that
"""
from fabric.api import *
import os
import time
import re

env.hosts = ['52.3.252.27', '54.160.117.45']
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_pack():
    """ This script generates a .tgz archive from contents of the
        web_static folder
    """
    local("mkdir -p versions")
    archive = "versions/web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S"))
    try:
        local("tar -cvzf {} web_static".format(archive))
        return archive
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
    run("sudo mkdir -p {}".format(releases_path))
    run("sudo tar -zxf /tmp/{}.tgz -C {}".format(file_name, releases_path))
    run("sudo cp -rf {}/web_static/* {}".format(releases_path, releases_path))
    run("sudo rm -r {}/web_static".format(releases_path))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(releases_path))
    print("New version deployed!")
    return True


def deploy():
    """ This function calls do_pack and do_deploy
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    status = do_deploy(archive_path)
    return status


def do_clean(number=0):
    """ This function deletes previous versions af web_static
    """
    ls_out = local("ls -1r versions", capture=True)
    ls_out = ls_out.split("\n")
    ls_server_out = run("ls -1r /data/web_static/releases | grep 'web_static'")
    ls_server_out = ls_server_out.split("\r\n")

    number = int(number)
    if number == 0:
        number += 1
    for file_name in ls_out[number:]:
        local("sudo rm versions/{}".format(file_name))

    for file_name in ls_server_out[number:]:
        run("sudo rm -r /data/web_static/releases/{}".format(file_name))
