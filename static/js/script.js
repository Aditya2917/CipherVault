function copyCipherText() {

    const cipherText = document.getElementById("cipherText");

    cipherText.select();

    navigator.clipboard.writeText(cipherText.value);

    alert("Cipher text copied successfully!");

}   


function clearFields() {

    document.querySelector("textarea[name='plaintext']").value = "";

    document.getElementById("cipherText").value = "";

    document.querySelector("input[name='secret_key']").value = "";

}
function downloadCipherText() {

    const cipherText = document.getElementById("cipherText").value;

    if (cipherText === "") {
        alert("No encrypted text available!");
        return;
    }

    const blob = new Blob([cipherText], { type: "text/plain" });

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);

    link.download = "encrypted_text.txt";

    link.click();

}