from library.lib import time, sys, os, platform

from module.encrypt.AES.GCM.main_gcm import *
from config.paths import *

import argparse

class FlagParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Secret -v.3.7.1- [Author by: seVen]')
        self.parser.add_argument('-e', type=str, required=False, help='Data encryption')
        self.parser.add_argument('-d', type=str, required=False, help='Data decryption')
        self.parser.add_argument('-p', type=str, required=False, help='Set password for encrypt or decrypt')
        
        # Парсим аргументы при создании объекта
        self.args = self.parser.parse_args()

class RunMainProject(FlagParser):
    def valid_flags(self):

        run_aesgcm = MainAesCgm()

        if self.args.e is not None:
            run_aesgcm.encrypt(file=self.args.e, password=self.args.p)
        elif self.args.d is not None:
            run_aesgcm.decrypt(file=self.args.d, password=self.args.p)


if __name__ == '__main__':
    create_main = RunMainProject()
    create_main.valid_flags()

