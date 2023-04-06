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
    now_n = datetime.now()
    str_now = now_n.strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    compress = local("tar -cvzf versions/web_static_{}.tar.gz web_static".
                     format(str_now))

    if compress is not None:
        return "/versions/web_static_{}.tar.gz".format(str_now)
    return None
