import pyfiglet
import os
import time
import sys

class MainConsoleInterface:

    def __init__(self, *, version: str) -> str:

        self._version = version
        self.f = pyfiglet.figlet_format("SECRET", font='slant')

        self.info_text = [
            '0 - [завершить программу]', 
            '1 - [шифрование/дешифрование]', 
            '2 - [кодирование/декодирование]',
            ]

    def create_main_menu(self):

        print(f"{self.f}\n                                {self._version}")
        print("-------------------------------------\n")

        for element in self.info_text:
            print(element)
        print(f"\n-------------------------------------\n")

        return input(f"{os.getlogin()}: ")





