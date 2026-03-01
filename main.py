from client.ui.interface import *
from module.encrypt.AES.GCM.main_gcm import *
import time
import sys

class RunMainProject:

    def __init__(self):
        self.__ui_result = create_interface.create_main_menu()

    def run_user_mode(self):

        if self.__ui_result == "0":
            print(f"DEBUG: завершение программы..")
            time.sleep(0.5)
            sys.exit()

        elif self.__ui_result == "1":
            #запуск main_gcm
            print(f"Запускаем gcm..")

        elif self.__ui_result == "2":
            #запуск кодирования
            print(f"Запускаем кодирование..")

if __name__ == '__main__':
    create_interface = MainConsoleInterface(version="v 2.1")
    create_main = RunMainProject().run_user_mode()
