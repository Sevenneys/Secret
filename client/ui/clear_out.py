
from library.lib import subprocess, os, platform
from typing import Callable

class ClearConsole:

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    FILE_PATH = os.path.join(ROOT_PATH, 'config', 'file', 'oc.txt')

    def __init__(self) -> None:
        self.__system = platform.system().lower()

    def clear(self):

        if self.__system == 'linux':
            syntax = ['clear']
        elif self.__system == 'windows':
            syntax = ['cls']

        try:
            result = subprocess.run(args=syntax, check=True, timeout=2, shell=False)
        except subprocess.CalledProcessError as er:
            print(f"ERROR: процесс ({os.getpid()}) завершился кодом выполнения: {er.returncode}")
        except subprocess.TimeoutExpired as er:
            print(f"WARNING: превышено время выполнения процесса ({os.getpid()})")

    

