#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers """

import time
from os.path import exists, isdir


def do_pack():
    """ A function that generates a .tgz archive """
    try:
        file_name = "versions/web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S"))
        if isdir("versions") is False:
            print("mkdir versions")
        print("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ A function that distributes an archive to your web servers """
    try:
        if not exists(archive_path):
            file_name = archive_path.split("/")[-1]
            file_no_ext = file_name.split(".")[0]
            path = "/data/web_static/releases/"
            print('./delete_me.py')
            print(archive_path, '/tmp/')
            print('mkdir -p {}{}/'.format(path, file_no_ext))
            print('tar -xzf /tmp/{} -C {}{}/'.format(file_name,
                                                   path, file_no_ext))
            print('rm /tmp/{}'.format(file_name))
            print('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_ext))
            print('rm -rf {}{}/web_static'.format(path, file_no_ext))
            print('rm -rf /data/web_static/current')
            print('ln -s {}{}/ /data/web_static/current'.format(
                path, file_no_ext))
            return True
        else:
            return False
    except Exception:
        return False


def deploy():
    """ A function that distributes an archive to your web servers """
    return do_deploy(do_pack())
deploy()
