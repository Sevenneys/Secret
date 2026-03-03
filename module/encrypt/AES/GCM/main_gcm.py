
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

from client.ui.interface import *
from client.ui.clear_out import *

from library.lib import os, sys, shutil

from module.encrypt.AES.GCM.path import *
from module.encrypt.AES.GCM.get_info import *
from module.encrypt.AES.GCM.json_coding import *
from module.encrypt.AES.GCM.KDF.pbkdf2 import *

class MainAesCgm:

    INFO_AES = ['0 - [шаг назад]', '1 - [шифрование]', '2 - [дешифрование]']

    create_interface = MainConsoleInterface()
    create_clear_out = ClearConsole()

    def __init__(self):
        self.__mode_aes = None
        self.__vectors = None

    def generate_vectors(self):

        key = AESGCM.generate_key(bit_length=192)
        nonce = os.urandom(12)

        self.__vectors = {'nonce': nonce, 'key': key}

    # ШИФРОВАНИЕ
    def encrypt(self):
        print("-------------------------------------")
        print(f"\nINFO: Укажите файл для шифрования --> \n")
        print("-------------------------------------")
        add_file_path = input(f"\n{os.getlogin()}: ")

        # Проверяем файл
        if os.path.exists(add_file_path):
            if os.path.isfile(add_file_path):
                for fi in os.path.split(add_file_path):
                    # Получаем полное имя файла 
                    get_file = str(fi)

                print(f"\nDEBUG: получен файл ({get_file})")
                time.sleep(0.5)
                print(f"DEBUG: размер файла ({os.path.getsize(add_file_path)}B)")
                    
                try:
                    # Разбиваем имя файла на список и создаём имя для директории
                    list_file = get_file.split(".")
                    get_title_file = f"{list_file[0]}(E)"
                    PATH_IS_DIRECTORY_FILE = os.path.join(PATH_DIRECTORY_FILES, get_title_file)

                    # Если такой директории нет, то работаем
                    if not os.path.exists(PATH_IS_DIRECTORY_FILE):
                        
                        # Создаём директорию
                        os.mkdir(PATH_IS_DIRECTORY_FILE)
                        # Получаем информацию и добавляем полное имя файла в файл с информацией
                        system_info = create_info_system()
                        system_info['file name'] = get_file
                        # Кодируем в json
                        codding_json = run_json(state=1, value=system_info)
                        # Получаем дескриптор, куда нужно записать этот файл с информацией
                        desc_sys_file = os.path.join(PATH_DIRECTORY_FILES, get_title_file, 'system_info.json')
                        # Вызываем функцию и передаём аргументы для записи файла
                        write_info(desc_sys_file, codding_json)

                        # Получаем дескрипторы для записи бинарных файлов (соль, хэш, ключ, зашифрованый файл)
                        get_path_salt = os.path.join(PATH_IS_DIRECTORY_FILE, 'salt_pass.bin')
                        get_path_pass_hash = os.path.join(PATH_IS_DIRECTORY_FILE, 'hash_pass.bin')
                        get_path_key = os.path.join(PATH_IS_DIRECTORY_FILE, 'aes_key.bin')
                        get_path_file_enc = os.path.join(add_file_path)

                        press_enter = input(f"\nДалее...")

                        # Вызываем функцию хэширования и передаем дескрипторы
                        self.create_clear_out.clear()
                        self.create_interface.create_logo()
                        create_hash_obj = KDF_Pbkdf2(path_salt=get_path_salt, path_hash=get_path_pass_hash)
                        create_hash_obj.create_hash_password()
                        self.create_clear_out.clear()
                        self.create_interface.create_logo()

                        # Вызываем функцию шифрования, передаём веторы и дескрипторы
                        self.generate_vectors()
                        # encrypt_gcm(vectors=self.__vectors, absolute_path_key=get_path_key, absolute_path_file=get_path_file_enc)

                        set_key = self.__vectors.get('key', 'Ключ: key - не найден..')
                        set_nonce = self.__vectors.get('nonce', 'Ключ: nonce - не найден..')
                        aesgcm = AESGCM(set_key)

                        print(f"\nDEBUG: устанавливаем ключ шифрования ({set_key})")
                        time.sleep(0.5)
                        print(f"DEBUG: устанавливаем случайные байты ({set_nonce})")
                        time.sleep(1)

                        try:
                            with open(get_path_key, 'wb') as f_wb:
                                f_wb.write(set_key)

                            with open(get_path_file_enc, 'rb') as f_rb:
                                data = f_rb.read()
                                print(f"DEBUG: длинна полученных данных ({len(data)})")

                            encrypt_text = aesgcm.encrypt(set_nonce, data, None)

                            with open(get_path_file_enc, 'wb') as f_wb:
                                f_wb.write(set_nonce + encrypt_text)
                                time.sleep(0.5)
                                print(f"DEBUG: шифруем данные из файла ( {data} --- 010010110 )")

                            time.sleep(1)
                            print(f"\nINFO: файл ({get_file}) - зашифрован")

                            press_enter = input(f"\nДалее..\n")

                            self.create_clear_out.clear()
                            self.create_interface.create_logo()

                        except Exception as err:
                            print(f"Er: {err}")

                    else:
                        print(f"\nERROR: файл с именем: {get_title_file} - уже зашифрован!")
                        print(f"INFO: Выберите другой файл или измените название текущему файлу.\n")
                except Exception as err:
                    print(f"ERROR: неожиданное исключение: {err}")    
            else:
                print(f"Выбранный объект - не является файлов..")
        else:
            print(f"Указанный файл - не найден..")
    
    def decrypt(self):

        self.create_clear_out.clear()
        self.create_interface.create_logo()

        print("-------------------------------------")
        print(f"\nINFO: Укажите файл для дешифрования >\n")
        print("-------------------------------------")
        encrypt_file = input(f"\n{os.getlogin()}: ")

        for fi in os.path.split(encrypt_file):
            get_file = str(fi)

        list_file = get_file.split(".")
        get_title_file = list_file[0] + '(E)'
        create_full_path = os.path.join(PATH_DIRECTORY_FILES, get_title_file)

        if os.path.isdir(create_full_path):

            self.create_clear_out.clear()
            self.create_interface.create_logo()

            print("-------------------------------------")
            print(f"\nINFO: Пароль для аутентификации ---->\n")
            print("-------------------------------------")
            confirm_password = input(f"\n{os.getlogin()}: ")

            get_salt = os.path.join(create_full_path, 'salt_pass.bin')
            get_origin_pass_hash = os.path.join(create_full_path, 'hash_pass.bin')
            get_path_key = os.path.join(create_full_path, 'aes_key.bin')

            try:
                with open(get_salt, 'rb') as f_rb:
                    origin_pass_salt = f_rb.read()
                with open(get_origin_pass_hash, 'rb') as f_rb:
                    origin_pass_hash = f_rb.read()

                create_hash_obj = KDF_Pbkdf2(path_salt=get_salt, path_hash=get_origin_pass_hash)
                result_in_hash = create_hash_obj.create_verify_hash_password(set_salt=origin_pass_salt, set_orig_hash=origin_pass_hash, set_password_confirm=confirm_password)

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

                        self.create_clear_out.clear()
                        self.create_interface.create_logo()
                        print("\nФайл успешно дешифрован!\n")

                    except InvalidTag as er:
                        print(f"При дешифровании файла произошла ошибка: {er}")
                else:
                    print(f"Ошибка - неверный пароль...")

            except Exception as er:
                    print(f"При получении исходного хэша, произошла ошибка: {er}")
        else:
            print(f"Директория: {create_full_path} - не существует!")

    def aescgm_interface(self):

        while True:

            try:
                print("-------------------------------------\n")

                for element in self.INFO_AES:
                    print(element)

                print(f"\n-------------------------------------\n")

                self.__mode_aes = input(f"{os.getlogin()}: ")
                    
            except KeyboardInterrupt:
                print(f"\n\nINFO: сочетание клавиш CTRL + C\nDEBUG: завершаем программу..\n")
                time.sleep(0.5)
                sys.exit()
            except Exception as er:
                print(f"ERROR: неожиданное исключение {er}")

            if self.__mode_aes == '0':
                self.create_clear_out.clear()
                return
            elif self.__mode_aes == '1':
                self.create_clear_out.clear()
                self.create_interface.create_logo()
                self.encrypt()
            elif self.__mode_aes == '2':
                self.decrypt()
            else:
                print(f"\nERROR: неверная комманда...\n")

    



