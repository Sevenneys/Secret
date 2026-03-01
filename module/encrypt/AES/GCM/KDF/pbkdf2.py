
from library.lib import hashlib, time, os

class KDF_Pbkdf2:

    def __init__(self, *, path_salt: str, path_hash: str) -> None:
        self.path_salt = path_salt
        self.path_hash = path_hash
    
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

        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password=in_password.encode('utf-8'),
            salt=salt,
            iterations=30000,
            dklen=256
        )

        try:
            with open(self.path_salt, "wb+") as f_wb:
                f_wb.write(salt)
            with open(self.path_hash, "wb+") as f_wb:
                f_wb.write(password_hash)

            print(f"\nINFO: пароль успешно создан и захэширован в бинарный файл!\n")

        except Exception as er:
            print("При записи файлов - произошла ошибка: {er}")
                          
    def create_verify_hash_password(self, *, set_salt: bytes, set_orig_hash: bytes, set_password_confirm: str) -> bool:

        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password=set_password_confirm.encode('utf-8'),
            salt=set_salt,
            iterations=30000,
            dklen=256
        )

        return password_hash == set_orig_hash
