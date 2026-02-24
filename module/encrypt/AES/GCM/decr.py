from lib import *
from path import *
import shutil
from KDF.pbkdf2 import create_verify_hash_password

def decrypt_gcm():

    encrypt_file = input(f"Укажите файл для дешифрования: ")

    for fi in os.path.split(encrypt_file):
        get_file = str(fi)

    list_file = get_file.split(".")
    get_title_file = list_file[0] + '(E)'
    create_full_path = os.path.join(PATH_DIRECTORY_FILES, get_title_file)

    if os.path.isdir(create_full_path):

        confirm_password = input(f"Пароль для аутентификации: ")

        get_salt = os.path.join(create_full_path, 'salt_pass.bin')
        get_origin_pass_hash = os.path.join(create_full_path, 'hash_pass.bin')
        get_path_key = os.path.join(create_full_path, 'aes_key.bin')

        try:
            with open(get_salt, 'rb') as f_rb:
                origin_pass_salt = f_rb.read()
            with open(get_origin_pass_hash, 'rb') as f_rb:
                origin_pass_hash = f_rb.read()

            result_in_hash = create_verify_hash_password(set_salt=origin_pass_salt, set_orig_hash=origin_pass_hash, set_password_confirm=confirm_password)
            if result_in_hash:

                try:
                    with open(get_path_key, 'rb') as f_rb:
                        set_key = f_rb.read()

                    with open(encrypt_file, 'rb') as f_rb:
                        get_full_data = f_rb.read()
                        nonce = get_full_data[:12]
                        encrypt_text = get_full_data[12:]

                except Exception as er:
                    print(f"Ошибка - файл {encrypt_file} не найден..")

                aescgm = AESGCM(set_key)

                try:
                    plaintext = aescgm.decrypt(nonce, encrypt_text, None)

                    with open(encrypt_file, "wb") as f_wb:
                        f_wb.write(plaintext)

                    shutil.rmtree(create_full_path)

                    print("Файл успешно дешифрован!")

                except InvalidTag as er:
                    print(f"При дешифровании файла произошла ошибка: {er}")

            else:
                print(f"Ошибка - неверный пароль...")

        except Exception as er:
                print(f"При получении исходного хэша, произошла ошибка: {er}")

    else:
        print(f"Директория: {create_full_path} - не существует!")
        

decrypt_gcm()



