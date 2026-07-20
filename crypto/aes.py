import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt_aes(plaintext, key):

    key = key.encode()

    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    return base64.b64encode(iv + encrypted).decode()


def decrypt_aes(ciphertext, key):

    key = key.encode()

    data = base64.b64decode(ciphertext)

    iv = data[:16]

    encrypted = data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

    return decrypted.decode()