import subprocess
import os

class ClearConsole:

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    FILE_PATH = os.path.join(ROOT_PATH, 'config', 'oc.txt')

    def __init__(self) -> None:
        self.__system = None

    def get_oc(self):

        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f_r:
                self.__system = f_r.read()

        except FileNotFoundError:
            print(f"ERROR: не удалось найти системный файл..")
        except Exception as er:
            print(f"ERROR: неожиданное исключение {er}")

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

    

