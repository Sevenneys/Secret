from lib import *

def encrypt_gcm(*, vectors: dict, absolute_path_key: str, absolute_path_file: str) -> bytes:
    
    set_key = vectors.get('key', 'Ключ: key - не найден..')
    set_nonce = vectors.get('nonce', 'Ключ: nonce - не найден..')
    aesgcm = AESGCM(set_key)

    print(absolute_path_file)

    try:
        with open(absolute_path_key, 'wb+') as f_wb:
            f_wb.write(set_key)

        with open(absolute_path_file, '+wb') as f_wb:

            data = f_wb.read()
            encrypt_text = aesgcm.encrypt(set_nonce, data, None)
            f_wb.write(set_nonce + encrypt_text)

    except Exception as err:
        print(f"Er: {err}")



