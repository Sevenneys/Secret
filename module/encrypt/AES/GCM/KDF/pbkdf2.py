import hashlib
import time
from module.encrypt.AES.GCM.path import *

def validation_of_password():

    cir = 'йцукенгшщзхъэждлорпавыфячсмитьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
    list_cir = list(cir)

    while True:

        password_file = input(f"Задайте пароль: ")

        if password_file == "":
           print("\nОшибка при вводе пароля: [пустая строка]\n")
           time.sleep(1)
        else:
            for i in password_file:
                if i in list_cir:
                    print("\nОшибка при вводе пароля: [кириллица - не подходящее значение]\n")
                    break
                else:
                    return password_file

def create_hash_password(*, absolute_path_salt: str, absolute_path_hash: str):

    in_password = validation_of_password()

    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password=in_password.encode('utf-8'),
        salt=salt,
        iterations=30000,
        dklen=256
    )

    try:
        with open(absolute_path_salt, "wb+") as f_wb:
            f_wb.write(salt)
        with open(absolute_path_hash, "wb+") as f_wb:
            f_wb.write(password_hash)
    except Exception as er:
        print("При записи файлов - произошла ошибка: {er}")
                    
    return
     
def create_verify_hash_password(set_salt: bytes, set_orig_hash: bytes, set_password_confirm: str) -> bool:

    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password=set_password_confirm.encode('utf-8'),
        salt=set_salt,
        iterations=30000,
        dklen=256
    )

    return password_hash == set_orig_hash
