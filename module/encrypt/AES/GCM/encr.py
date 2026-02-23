from lib import *
from path import *
from get_info import *
from json_coding import *

def write_sys_info(absolute_path: str, sys_info: json) -> json:

    if not os.path.exists(absolute_path):
        try:

            with open(absolute_path, "w+", encoding="utf-8") as f_wr:
                f_wr.write(sys_info)

        except Exception as err:
            print(f"При записи файла произошла ошибка: {Exception}")

def generate_vectors():

    key = AESGCM.generate_key(bit_length=192)
    nonce = os.urandom(12)

    return {
        'nonce':nonce,
        'key':key,
    }

def encrypted_gcm(*, vectors: dict):

    if all(key in vectors for key in['nonce', 'key']):
        
        add_file_path = input(f"Укажите файл для шифрования: ")

        if os.path.exists(add_file_path):
            if os.path.isfile(add_file_path):
                for fi in os.path.split(add_file_path):
                    get_file = str(fi)
                
                try:

                    list_file = get_file.split(".")
                    get_title_file = f"{list_file[0]}(E)"
                    PATH_IS_DIRECTORY_FILE = os.path.join(PATH_DIRECTORY_FILES, get_title_file)
                    os.mkdir(PATH_IS_DIRECTORY_FILE)

                    try:
                        system_info = create_info_system()
                        codding_json = run_json(state=1, value=system_info)
                        desc_sys_file = os.path.join(PATH_DIRECTORY_FILES, 'system_info.json')

                        write_sys_info(desc_sys_file, codding_json)

                    except Exception as er:
                        print(f"Произошла ошибка: {er}")
                    
                except Exception as err:
                    print(f"\nОшибка: файл с именем: {get_title_file} - уже зашифрован!")
                    print(f"Выберите другой файл или измените название текущему файлу.\n")

                add_password_file = input(f"Задайте пароль: ")

            else:
                print(f"Выбранный объект - не является файлов..")
        else:
            print(f"Указанный файл - не найден..")


    else:
        print("Ошибка: отсутствуют ключи для работы в режиме GCM..")

a = generate_vectors()
encrypted_gcm(vectors=a)


