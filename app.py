from crypto.aes import encrypt_aes, decrypt_aes
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    encrypted_text = ""
    plaintext = ""
    secret_key = ""

    if request.method == "POST":
        plaintext = request.form["plaintext"]
        secret_key = request.form["secret_key"]
        action = request.form["action"]

    try:
        if len(secret_key) not in [16, 24, 32]:
            raise ValueError("AES key must be 16, 24, or 32 characters long.")
        if action == "encrypt":
            encrypted_text = encrypt_aes(plaintext, secret_key)
        elif action == "decrypt":
            encrypted_text = decrypt_aes(plaintext, secret_key)
    except Exception as e:
        encrypted_text = str(e)

    return render_template(
    "index.html",
    encrypted_text=encrypted_text,
    plaintext=plaintext,
    secret_key=secret_key
)
if __name__ == "__main__":
    app.run(debug=True)