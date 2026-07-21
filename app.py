import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from utils.algorithm_manager import ALGORITHMS

from crypto.rsa import (
    generate_keys,
    encrypt_rsa,
    decrypt_rsa
)

app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "ciphervault_secret_key"
)


@app.route("/", methods=["GET", "POST"])
def home():

    # =========================
    # GET REQUEST
    # =========================

    if request.method == "GET":

        data = session.pop("result", None)

        if data:

            return render_template(
                "dashboard.html",
                algorithm=data["algorithm"],
                plaintext=data["plaintext"],
                encrypted_text=data["encrypted_text"],
                secret_key=data["secret_key"],
                public_key=data["public_key"],
                private_key=data["private_key"],
                status_type=data["status_type"],
                status_message=data["status_message"]
            )
        session.pop("public_key", None)
        session.pop("private_key", None)
        return render_template(
    "dashboard.html",
    algorithm="AES",
    plaintext="",
    encrypted_text="",
    secret_key="",
    public_key=session.get("public_key", ""),
    private_key=session.get("private_key", ""),
    status_type="READY",
    status_message="Select an algorithm."
)
    # =========================
    # POST REQUEST
    # =========================

    plaintext = request.form.get("plaintext", "")

    secret_key = request.form.get("secret_key", "")

    public_key = request.form.get(
        "public_key",
        session.get("public_key", "")
    )

    private_key = request.form.get(
        "private_key",
        session.get("private_key", "")
    )

    algorithm = request.form.get(
        "algorithm",
        "AES"
    )

    action = request.form.get(
        "action",
        "encrypt"
    )

    encrypted_text = ""

    status_type = "READY"

    status_message = ""

    try:

        # =====================
        # RSA
        # =====================

        if algorithm == "RSA":

            if action == "generate_keys":

                public_key, private_key = generate_keys()

                session["public_key"] = public_key

                session["private_key"] = private_key

                status_type = "SUCCESS"

                status_message = "RSA Key Pair Generated Successfully."

                session["result"] = {

                    "algorithm": "RSA",

                    "plaintext": "",

                    "encrypted_text": "",

                    "secret_key": "",

                    "public_key": public_key,

                    "private_key": private_key,

                    "status_type": status_type,

                    "status_message": status_message

                }

                return redirect(url_for("home"))
            elif action == "encrypt":

                encrypted_text = encrypt_rsa(
                    plaintext,
                    public_key
                )

                status_type = "SUCCESS"
                status_message = "RSA Encryption Successful."

            elif action == "decrypt":

                encrypted_text = decrypt_rsa(
                    plaintext,
                    private_key
                )

                status_type = "SUCCESS"
                status_message = "RSA Decryption Successful."

        # =====================
        # AES / DES
        # =====================

        else:

            selected_algorithm = ALGORITHMS[algorithm]

            if len(secret_key) not in selected_algorithm["key_lengths"]:

                raise ValueError(
                    f"{algorithm} key must be "
                    f"{selected_algorithm['key_lengths']} characters long."
                )

            if action == "encrypt":

                encrypted_text = selected_algorithm["encrypt"](
                    plaintext,
                    secret_key
                )

                status_message = (
                    f"{algorithm} Encryption Successful."
                )

            else:

                encrypted_text = selected_algorithm["decrypt"](
                    plaintext,
                    secret_key
                )

                status_message = (
                    f"{algorithm} Decryption Successful."
                )

            status_type = "SUCCESS"

    except Exception as e:

        encrypted_text = ""

        status_type = "ERROR"

        status_message = str(e)

    session["result"] = {

        "algorithm": algorithm,

        "plaintext": plaintext,

        "encrypted_text": encrypted_text,

        "secret_key": secret_key,

        "public_key": public_key,

        "private_key": private_key,

        "status_type": status_type,

        "status_message": status_message

    }

    return redirect(url_for("home"))


@app.route("/reset")
def reset():

    session.clear()

    return redirect(url_for("home"))


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)