from crypto.aes import encrypt_aes, decrypt_aes
from crypto.des import encrypt_des, decrypt_des

ALGORITHMS = {

    "AES": {
        "encrypt": encrypt_aes,
        "decrypt": decrypt_aes,
        "key_lengths": [16, 24, 32]
    },

    "DES": {
        "encrypt": encrypt_des,
        "decrypt": decrypt_des,
        "key_lengths": [8]
    }

}