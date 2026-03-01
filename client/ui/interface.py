
from library.lib import pyfiglet, os, time, sys

class MainConsoleInterface:

    INFO = ['0 - [завершить программу]', '1 - [шифрование/дешифрование]', '2 - [кодирование/декодирование]']

    def __init__(self):
        self._version = 'v 3.1.5'
        self._banner = pyfiglet.figlet_format("SECRET", font='slant')

    # сделать - берём версию из файла переменного окружения, в коде вручную не пишем!
    def create_logo(self):
        print(f"\n{self._banner}\n                              {self._version}")
        
    def create_main_menu(self):

        try:
            print("-------------------------------------\n")

            for element in self.INFO:
                print(element)

            print(f"\n-------------------------------------\n")

            return input(f"{os.getlogin()}: ")
                
        except KeyboardInterrupt:
            print(f"\n\nINFO: сочетание клавиш CTRL + C\nDEBUG: завершаем программу..\n")
            time.sleep(0.5)
            sys.exit()
        except Exception as er:
            print(f"ERROR: неожиданное исключение {er}")




        





