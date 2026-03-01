import pyfiglet
import os
import time
import sys

class MainConsoleInterface:

    INFO = ['0 - [завершить программу]', '1 - [шифрование/дешифрование]', '2 - [кодирование/декодирование]']
    VALID_MODE = ['0', '1', '2']

    def __init__(self, *, version: str) -> None:
        self._version = version
        self._banner = pyfiglet.figlet_format("SECRET", font='slant')

    def create_logo(self):
        print(f"\n{self._banner}\n                                {self._version}")
        
    def create_main_menu(self):

        while True:
            try:
                print("-------------------------------------\n")

                for element in self.INFO:
                    print(element)

                print(f"\n-------------------------------------\n")

                user = input(f"{os.getlogin()}: ")

                if user not in self.VALID_MODE:
                    print(f"ERROR: неверная комманда...\n")
                    time.sleep(0.5)
                else:
                    return user
                
            except KeyboardInterrupt:
                print(f"\n\nINFO: сочетание клавиш CTRL + C\nDEBUG: завершаем программу..\n")
                time.sleep(0.5)
                sys.exit()
            except Exception as er:
                print(f"ERROR: неожиданное исключение {er}")

        





