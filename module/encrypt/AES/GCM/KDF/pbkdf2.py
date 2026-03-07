
from library.lib import hashlib, time, os, shutil

class KDF_Pbkdf2:

    def __init__(self, *, path_salt: str, path_hash: str, path_dir: str) -> None:
        self.path_salt = path_salt
        self.path_hash = path_hash
        self.path_dir = path_dir
    
    def create_and_validation_of_password(self):

        while True:
            print("-------------------------------------")
            print(f"\nINFO: Задайте пароль --------------->\n")
            print("-------------------------------------")
            password_file = input(f"\n{os.getlogin()}: ")


            if password_file == "":
                print("\nОшибка при вводе пароля: [пустая строка]\n")
                time.sleep(1)
            else:
                return password_file

    def create_hash_password(self):

        in_password = self.create_and_validation_of_password()

        print(f"\nINFO: длина пароля {len(in_password)} символов")
        time.sleep(0.5)
        print(f"DEBUG: создаём хэш")

        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password=in_password.encode('utf-8'),
            salt=salt,
            iterations=30000,
            dklen=256
        )

        time.sleep(0.5)
        print(f"DEBUG: хэш пароля ({password_hash})")
        print(f"DEBUG: соль ({salt})")

        try:
            with open(self.path_salt, "wb+") as f_wb:
                f_wb.write(salt)
            with open(self.path_hash, "wb+") as f_wb:
                f_wb.write(password_hash)

            print(f"\nINFO: хэш успешно записан в бинарный файл (hash_pass.bin)\n")
            time.sleep(1)

        except Exception as er:
            shutil.rmtree(self.path_dir)
            print("При записи файлов - произошла ошибка: {er}")
        except KeyboardInterrupt:
            shutil.rmtree(self.path_dir)
            print("DEBUG: принудительное завершение программы")
                          
    def create_verify_hash_password(self, *, set_salt: bytes, set_orig_hash: bytes, set_password_confirm: str) -> bool:

        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password=set_password_confirm.encode('utf-8'),
            salt=set_salt,
            iterations=30000,
            dklen=256
        )

        return password_hash == set_orig_hash
