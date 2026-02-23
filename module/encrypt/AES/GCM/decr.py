from lib import *
from path import *

def decrypt_gcm():

    encrypt_file = input(f"Укажите файл для дешифрования: ")

    for fi in os.path.split(encrypt_file):
        get_file = str(fi)

    list_file = get_file.split(".")
    get_title_file = list_file[0] + '(E)'
    create_full_path = os.path.join(PATH_DIRECTORY_FILES, get_title_file)

    if os.path.isdir(create_full_path):
        print(f"Директория: {create_full_path} - существует!")
    else:
        print(f"Директория: {create_full_path} - не существует!")

decrypt_gcm()



