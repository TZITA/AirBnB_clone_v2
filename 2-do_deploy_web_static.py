#!/usr/bin/python3
""" Deploy web static archive."""
from fabric.api import *
from datetime import datetime
import os.path


env.hosts = ['34.224.62.19', '54.166.130.58']


def do_deploy(archive_path):
    """Deploy web files to server."""
    try:
        if not (os.path.exists(archive_path)):
            return False

        put(archive_path, '/tmp/')

        timeext = archive_path[11:25]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.
            format(timeext))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/\
            releases/web_static_{}/'.format(timeext, timeext))

        run('sudo rm /tmp/web_static_{}.tgz'.format(timeext))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/'.format(timeext, timeext))

        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(timeext))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/web_static_{}/ \
            /data/web_static/current'.format(timeext))

    except Exception:
        return False
    return True
