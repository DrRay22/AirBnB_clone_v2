#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ['35.231.33.237', '34.74.155.163']
env.user = "ubuntu"


def deploy():
    """ DEPLOYS """
    try:
        archive_path = do_pack()
    except:
        return False

    return do_deploy(archive_path)
