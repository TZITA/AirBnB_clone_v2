#!/usr/bin/python3
"""
    A fabric script that generates a .tgz archive
    from the contents of the web_static.
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    A function to compress and store the contents
    of the web_static files.

    Returns: The path of tar file.
    """
    now_n = datetime.utcnow()
    str_now = now_n.strftime("%Y%m%d%H%M%S")
    file_c = "versions/web_static_{}.tgz".format(str_now)

    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_c))
        return file_c

    except Exception:
        return None
