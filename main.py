from library.lib import time, sys, os, platform

from client.ui.interface import *
from client.ui.clear_out import *
from module.encrypt.AES.GCM.main_gcm import *

class RunMainProject:

    # изменить на общий файл путей.
    ROOT_PROJECT = os.path.dirname(__file__)
    FILE_OC = os.path.join(ROOT_PROJECT, 'config', 'oc.txt')
    VALID_MODE = ['0', '1', '2']

    def __init__(self):
        self._logo = create_interface.create_logo()
        self.__ui_result = create_interface.create_main_menu()

    def valid_out_user(self):
        if self.__ui_result not in self.VALID_MODE:
            print(f"\nERROR: неверная комманда...\n")
            time.sleep(0.5)
            create_clear_out.clear()
            
    def run_user_mode(self):

        if self.__ui_result == "0":
            print(f"\nDEBUG: завершение программы..\n")
            time.sleep(0.5)
            create_clear_out.clear()
            sys.exit()

        elif self.__ui_result == "1":

            create_aes_main = MainAesCgm()
            create_clear_out.clear()
            create_interface.create_logo()
            create_aes_main.aescgm_interface()
            create_clear_out.clear()

        elif self.__ui_result == "2":
            #запуск кодирования
            print(f"Запускаем кодирование..")

if __name__ == '__main__':

    create_interface = MainConsoleInterface()
    create_clear_out = ClearConsole()

    create_clear_out.clear()

    while True:

        create_main = RunMainProject()
        create_main.valid_out_user()
        create_main.run_user_mode()

