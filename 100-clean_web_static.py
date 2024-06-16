#!/usr/bin/python3
#deletes out of date archieves
import os
from fabric.api import *

env.hosts = ["100.25.109.145", "100.26.17.68"]

def do_clean(number=0):
    """deletes out of date archieves.

    Args:
    (int) number: number
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archieves.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archieves.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
