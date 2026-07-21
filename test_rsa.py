from crypto.rsa import generate_keys, encrypt_rsa, decrypt_rsa

public_key, private_key = generate_keys()

message = "Hello CipherVault"

cipher = encrypt_rsa(message, public_key)

print("Encrypted:\n")
print(cipher)

plain = decrypt_rsa(cipher, private_key)

print("\nDecrypted:\n")
print(plain)