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