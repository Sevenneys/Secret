import pyfiglet
import os
import time
import sys

class MainConsoleInterface:

    def __init__(self, *, version: str) -> str:

        self._version = version
        self.f = pyfiglet.figlet_format("SECRET", font='slant')

        self.info_data = {
            'info':['0 - [завершить программу]', '1 - [шифрование/дешифрование]', '2 - [кодирование/декодирование]',],
            'mode': ['0', '1', '2']
        }

    def create_main_menu(self):
        print(f"{self.f}\n                                {self._version}")

        while True:
            try:
                print("-------------------------------------\n")

                for element in self.info_data.get('info'):
                    print(element)

                print(f"\n-------------------------------------\n")

                user = input(f"{os.getlogin()}: ")

                if user not in self.info_data.get('mode'):
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

        





