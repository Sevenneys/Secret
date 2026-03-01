from module.encrypt.AES.GCM.lib import *

def encrypt_gcm(*, vectors: dict, absolute_path_key: str, absolute_path_file: str) -> bytes:
    
    set_key = vectors.get('key', 'Ключ: key - не найден..')
    set_nonce = vectors.get('nonce', 'Ключ: nonce - не найден..')
    aesgcm = AESGCM(set_key)

    try:
        with open(absolute_path_key, 'wb') as f_wb:
            f_wb.write(set_key)

        with open(absolute_path_file, 'rb') as f_rb:
            data = f_rb.read()

        encrypt_text = aesgcm.encrypt(set_nonce, data, None)

        with open(absolute_path_file, 'wb') as f_wb:
            f_wb.write(set_nonce + encrypt_text)

    except Exception as err:
        print(f"Er: {err}")



