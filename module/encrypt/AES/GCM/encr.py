from lib import *

def generate_vectors():

    key = AESGCM.generate_key(bit_length=192)
    now_is_password = "Qwerty12345"
    nonce = os.urandom(12)

    return {
        "nonce":nonce,
        "key":key,
        "password":now_is_password
    }

# def encrypted_gcm(key, password):
#     pass

