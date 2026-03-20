
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

from library.lib import os, sys, shutil

from globals.get_info import *
from globals.json_coding import *
from config.paths import *
from module.encrypt.AES.GCM.KDF.pbkdf2 import *

class MainAesCgm:

    def __init__(self):
        self.__mode_aes = None
        self.__vectors = None

    def generate_vectors(self):

        key = AESGCM.generate_key(bit_length=192)
        nonce = os.urandom(12)

        self.__vectors = {'nonce': nonce, 'key': key}

    # ШИФРОВАНИЕ
    def encrypt(self, *, file: str, password: str):
        add_file_path = file

        # Проверяем файл
        if os.path.exists(add_file_path):
            if os.path.isfile(add_file_path):
                get_file = os.path.basename(add_file_path)

                print(f"\n[DEBUG] --- FILE RECEIVED --- [DEBUG]")
                time.sleep(0.5)

                try:
                    # Разбиваем имя файла на список и создаём имя для директории
                    title_file = get_file.split(".")[0]
                    path_to_file = os.path.split(add_file_path)[0] + '/'
                    PATH_IS_DIRECTORY_FILE = os.path.join(PATH_DIRECTORY_FILES, title_file)

                    # Если такой директории нет, то работаем
                    if not os.path.exists(PATH_IS_DIRECTORY_FILE):
                        
                        os.mkdir(PATH_IS_DIRECTORY_FILE)
                        system_info = create_info_system(get_file)
                        codding_json = run_json(state=1, value=system_info)
                        desc_sys_file = os.path.join(PATH_DIRECTORY_FILES, title_file, 'system_info.json')
                        write_info(desc_sys_file, codding_json)

                        # Получаем дескрипторы для записи бинарных файлов (соль, хэш, ключ, зашифрованый файл)
                        get_path_salt = os.path.join(PATH_IS_DIRECTORY_FILE, 'salt_pass.bin')
                        get_path_pass_hash = os.path.join(PATH_IS_DIRECTORY_FILE, 'hash_pass.bin')
                        get_path_key = os.path.join(PATH_IS_DIRECTORY_FILE, 'aes_key.bin')

                        get_path_file_enc = path_to_file + title_file + '.oxo'

                        # Вызываем функцию хэширования и передаем дескрипторы
                        create_hash_obj = KDF_Pbkdf2(path_salt=get_path_salt, path_hash=get_path_pass_hash, path_dir=PATH_IS_DIRECTORY_FILE)
                        create_hash_obj.create_hash_password(cr_password=password)
                        
                        # Вызываем функцию шифрования, передаём веторы и дескрипторы
                        self.generate_vectors()
                        # encrypt_gcm(vectors=self.__vectors, absolute_path_key=get_path_key, absolute_path_file=get_path_file_enc)

                        set_key = self.__vectors.get('key', 'Ключ: key - не найден..')
                        set_nonce = self.__vectors.get('nonce', 'Ключ: nonce - не найден..')
                        aesgcm = AESGCM(set_key)

                        try:
                            with open(get_path_key, 'wb') as f_wb:
                                f_wb.write(set_key)

                            with open(add_file_path, 'rb') as f_rb:
                            
                                data = f_rb.read()
                                encrypt_text = aesgcm.encrypt(set_nonce, data, None)

                            with open(get_path_file_enc, 'wb') as f_wb:
                                f_wb.write(set_nonce + encrypt_text)
                            os.remove(add_file_path)

                            print("""             
-1-0-1-0-1-0-1-0-1-0-1-0
-0-1-0-1-0-1-0-1-0-1-0-1
-1-0-1-0-1-0-1-0-1-0-1-0
-0-1-0-1-0-1-0-1-0-1-0-1
                            """)
                            time.sleep(0.5)

                            print(f"[DEBUG] --- FILE SUCCESSFULLY ENCRYPTED --- [DEBUG]\n")

                        except Exception as err:
                            shutil.rmtree(PATH_IS_DIRECTORY_FILE)
                            print(f"[ERROR] --- {err} --- [ERROR]")

                    else:
                        print(f"\n[WARNING] --- THE SPECIFIED FILE IS ALREADY ENCRYPTED --- [WARNING]\n")
                except Exception as err:
                    shutil.rmtree(PATH_IS_DIRECTORY_FILE)
                    print(f"[ERROR]--- {err} --- [ERROR]")    
            else:
                print(f"\n[WARNING] --- THE SELECTED OBJECT IS NOT A FILE --- [WARNING]\n")
        else:
            print(f"\n[WARNING] --- THE SPECIFIED FILE WAS NOT FOUND --- [WARNING]\n")
    
    def decrypt(self, *, file: str, password: str ):

        encrypt_file = file

        for fi in os.path.split(encrypt_file):
            get_file = str(fi)

        print(f"\n[DEBUG] --- FILE RECEIVED --- [DEBUG]")
        time.sleep(0.5)

        list_file = get_file.split(".")
        get_title_file = list_file[0]
        create_full_path = os.path.join(PATH_DIRECTORY_FILES, get_title_file)

        path_system_info = create_full_path + '/system_info.json'

        with open(path_system_info, 'r+', encoding='utf-8') as r_w:
            json_data = r_w.read()
            decodding_data_systeminfo = run_json(state=0, value=json_data)

        path_to_file = os.path.split(encrypt_file)[0] + '/'
        origin_file = decodding_data_systeminfo.get('file name')
        decrypt_file = path_to_file + origin_file

        if os.path.isdir(create_full_path):

            confirm_password = password

            get_salt = os.path.join(create_full_path, 'salt_pass.bin')
            get_origin_pass_hash = os.path.join(create_full_path, 'hash_pass.bin')
            get_path_key = os.path.join(create_full_path, 'aes_key.bin')

            try:
                with open(get_salt, 'rb') as f_rb:
                    origin_pass_salt = f_rb.read()
                with open(get_origin_pass_hash, 'rb') as f_rb:
                    origin_pass_hash = f_rb.read()

                create_hash_obj = KDF_Pbkdf2(path_salt=get_salt, path_hash=get_origin_pass_hash, path_dir=create_full_path)
                result_in_hash = create_hash_obj.create_verify_hash_password(set_salt=origin_pass_salt, set_orig_hash=origin_pass_hash, set_password_confirm=confirm_password)

                if result_in_hash:

                    try:
                        with open(get_path_key, 'rb') as f_rb:
                            set_key = f_rb.read()

                        with open(encrypt_file, 'rb') as f_rb:
                            get_full_data = f_rb.read()
                            nonce = get_full_data[:12]
                            encrypt_text = get_full_data[12:]

                        aescgm = AESGCM(set_key)

                        print("""             
-A-b-C-d-E-f-G-i-L-k-M-n
-0-1-2-3-4-5-6-7-8-9-!--
-@-#-$-%-^-&-*-(-)-;-:-'
-А-б-В-г-Д-е-Ж-з-Н-о-К-л
                        """)
                        time.sleep(0.5)

                    except Exception as er:
                        print(f"\n[WARNING] --- THE SPECIFIED FILE WAS NOT FOUND --- [WARNING]")

                    try:
                        plaintext = aescgm.decrypt(nonce, encrypt_text, None)

                        with open(decrypt_file, "wb") as f_wb:
                            f_wb.write(plaintext)

                        os.remove(encrypt_file)
                        shutil.rmtree(create_full_path)

                        print(f"[DEBUG] --- FILE SUCCESSFULLY DECRYPTED --- [DEBUG]\n")

                    except InvalidTag as er:
                        print(f"\n[ERROR] --- {er} --- [ERROR]\n")
                else:
                    print(f"\n[WARNING] --- INCORRECT PASSWORD --- [WARNING]\n")

            except Exception as er:
                    print(f"\n[ERROR] --- FAILED TO OBTAIN ORIGINAL HASH {er} --- [ERROR]\n")
        else:
            print(f"\n[WARNING] --- FILE DIRECTORY DOES NOT EXIST --- [WARNING]\n")


    



