import pyfiglet
import os
import time
import sys

class ConsoleInterface:

    f = pyfiglet.figlet_format("SECRET", font='slant')

    def __init__(self, *, version: str) -> str:

        self._version = version

    def create_main_menu(self):

        print(self.f)
        print(f"                                {self._version}")
        print("-------------------------------------")

        print()

        print("0 - [завершить программу]")
        print("1 - [шифрование/дешифрование]")
        print("2 - [кодированние/декодированние]")

        print()
        print("-------------------------------------")
        print()

        return input(f"{os.getlogin()}: ")

    def encrypt_interface(self):

        print()

        print("-------------------------------------")
        print("0 - [назад]")
        print("1 - [AES]")
        print("-------------------------------------")

        print()

        return input(f"{os.getlogin()}: ")




