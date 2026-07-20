import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt_des(plaintext, key):

    key = key.encode()

    iv = get_random_bytes(8)

    cipher = DES.new(key, DES.MODE_CBC, iv)

    encrypted = cipher.encrypt(
        pad(plaintext.encode(), DES.block_size)
    )

    return base64.b64encode(iv + encrypted).decode()


def decrypt_des(ciphertext, key):

    key = key.encode()

    data = base64.b64decode(ciphertext)

    iv = data[:8]

    encrypted = data[8:]

    cipher = DES.new(key, DES.MODE_CBC, iv)

    decrypted = unpad(
        cipher.decrypt(encrypted),
        DES.block_size
    )

    return decrypted.decode()