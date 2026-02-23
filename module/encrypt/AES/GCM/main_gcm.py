from lib import *
from path import *
from get_info import *
from json_coding import *
from KDF.pbkdf2 import *
from encr import *

def generate_vectors():

    key = AESGCM.generate_key(bit_length=192)
    nonce = os.urandom(12)

    return {
        'nonce':nonce,
        'key':key,
    }

def main_gcm():

    add_file_path = input(f"Укажите файл для шифрования: ")

    if os.path.exists(add_file_path):
        if os.path.isfile(add_file_path):
            for fi in os.path.split(add_file_path):
                get_file = str(fi)
                
            try:
                list_file = get_file.split(".")
                get_title_file = f"{list_file[0]}(E)"
                PATH_IS_DIRECTORY_FILE = os.path.join(PATH_DIRECTORY_FILES, get_title_file)

                if not os.path.exists(PATH_IS_DIRECTORY_FILE):

                    os.mkdir(PATH_IS_DIRECTORY_FILE)
                    system_info = create_info_system()
                    system_info['file name'] = get_file
                    codding_json = run_json(state=1, value=system_info)
                    desc_sys_file = os.path.join(PATH_DIRECTORY_FILES, get_title_file, 'system_info.json')
                    write_info(desc_sys_file, codding_json)

                    get_path_salt = os.path.join(PATH_IS_DIRECTORY_FILE, 'salt_pass.bin')
                    get_path_pass_hash = os.path.join(PATH_IS_DIRECTORY_FILE, 'hash_pass.bin')
                    get_path_key = os.path.join(PATH_IS_DIRECTORY_FILE, 'aes_key.bin')
                    get_path_file_enc = os.path.join(add_file_path)

                    vectors = generate_vectors()
                    hash_passw = create_hash_password(absolute_path_salt=get_path_salt, absolute_path_hash=get_path_pass_hash)
                    encrypt_gcm(vectors=vectors, absolute_path_key=get_path_key, absolute_path_file=get_path_file_enc)

                else:
                    print(f"\nОшибка: файл с именем: {get_title_file} - уже зашифрован!")
                    print(f"Выберите другой файл или измените название текущему файлу.\n")
            except Exception as err:
                print(f"При работе программы - произошла ошибка: {err}")    
        else:
            print(f"Выбранный объект - не является файлов..")
    else:
        print(f"Указанный файл - не найден..")

main_gcm()


