from lib import os, platform
from json_coding import *

def create_info_system():

    oc = platform.system()
    username = os.getlogin()
    host = platform.node()

    return {'oc': oc, 'username': username, 'host': host}


