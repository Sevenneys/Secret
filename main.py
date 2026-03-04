from library.lib import time, sys, os, platform

from client.ui.interface import *
from client.ui.clear_out import *
from module.encrypt.AES.GCM.main_gcm import *
from config.objects import *

class RunMainProject:

    # изменить на общий файл путей.
    ROOT_PROJECT = os.path.dirname(__file__)
    FILE_OC = os.path.join(ROOT_PROJECT, 'config', 'oc.txt')
    VALID_MODE = ['0', '1', '2']

    def __init__(self):
        self._logo = None
        self.__ui_result = None

    def valid_out_user(self, func_param):

        if self.__ui_result not in self.VALID_MODE:
            print(f"\nERROR: неверная комманда...\n")
            time.sleep(0.5)
            create_clear_out.clear()
            
    def run_user_mode(self):

        self._logo = create_interface.create_logo()
        self.__ui_result = create_interface.create_main_menu()
        self.valid_out_user(self.__ui_result)

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

    while True:
        create_clear_out.clear()
        create_main = RunMainProject().run_user_mode()

