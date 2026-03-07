from library.lib import os, platform
from globals.json_coding import *

# Сделать класс

def create_info_system(file_name):

    oc = platform.system()
    username = os.getlogin()
    host = platform.node()

    return {'oc': oc, 'username': username, 'host': host, 'file name': file_name}

def write_info(absolute_path: str, sys_info: str) -> str:

    if not os.path.exists(absolute_path):
        try:
            with open(absolute_path, "w+", encoding="utf-8") as f_wr:
                f_wr.write(sys_info)
                
        except Exception as err:
            print(f"При записи файла произошла ошибка: {Exception}")
