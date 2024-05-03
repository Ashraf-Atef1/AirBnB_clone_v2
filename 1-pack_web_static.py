#!/usr/bin/python3
import time
from fabric.api import local
from os.path import isdir

def do_pack():
    try:
        file_name = f"versions/web_static_{time.strftime("%Y%m%d%H%M%S")}.tgz"
        if isdir("versions") is False:
            local("mkdir versions")
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except:
        return None
