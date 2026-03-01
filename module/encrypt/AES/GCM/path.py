from library.lib import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
PATH_DIRECTORY_FILES = os.path.join(ROOT_PATH, 'client', 'directory_of_files')
PATH_MODULE_FILE = os.path.join(ROOT_PATH, 'module', 'get_info.py')