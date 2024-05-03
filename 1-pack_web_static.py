#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
import time
from fabric.api import local
from os.path import isdir


def do_pack():
    """ A function that generates a .tgz archive """
    try:
        file_name = f"versions/web_static_{time.strftime("%Y%m%d%H%M%S")}.tgz"
        if isdir("versions") is False:
            local("mkdir versions")
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except Exception:
        return None
