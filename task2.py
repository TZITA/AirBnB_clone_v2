#!/usr/bin/python3
""" """
from fabric.api import *
from os import path


def do_deploy(archive_path):
    """ """
    if not (path.exists(archive_path)):
        return False
    


