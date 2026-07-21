function showToast(message){

    document.getElementById("toastMessage").innerHTML=message;

    const toast=new bootstrap.Toast(
        document.getElementById("liveToast")
    );

    toast.show();

}/* ==========================================
            CIPHERVAULT SCRIPT
========================================== */

const cards = document.querySelectorAll(".algorithm-card");
const algorithmInput = document.getElementById("algorithm");

const secretKeySection = document.getElementById("secretKeySection");
const rsaSection = document.getElementById("rsaSection");

const statusMessage = document.getElementById("statusMessage");
const statusBadge = document.getElementById("statusBadge");

const currentAlgorithm = document.getElementById("currentAlgorithm");

const secretKeyInput = document.getElementById("secretKeyInput");
const toggleSecretKey = document.getElementById("toggleSecretKey");

/*==========================================
        COPY
==========================================*/

function copyCipherText(){

    const cipher = document.getElementById("cipherText").value;

    if(cipher===""){

        showToast("⚠ Nothing to copy.");

        return;

    }

    navigator.clipboard.writeText(cipher);

    showToast("✅ Cipher text copied.");

}

/*==========================================
        DOWNLOAD
==========================================*/

function downloadCipherText(){

    const cipher=document.getElementById("cipherText").value;

    if(cipher===""){

        showToast("⚠ Nothing to download.");

        return;

    }

    const blob=new Blob([cipher],{type:"text/plain"});

    const link=document.createElement("a");

    link.href=URL.createObjectURL(blob);

    link.download="ciphertext.txt";

    link.click();

}

/*==========================================
        CLEAR
==========================================*/

function clearFields(){

    document.querySelector("textarea[name='plaintext']").value="";

    document.getElementById("cipherText").value="";

    const key=document.querySelector("input[name='secret_key']");

    if(key) key.value="";

    const publicKey=document.querySelector("textarea[name='public_key']");

    const privateKey=document.querySelector("textarea[name='private_key']");

    if(publicKey) publicKey.value="";

    if(privateKey) privateKey.value="";

    statusBadge.innerHTML="READY";

    statusMessage.innerHTML="Ready for encryption.";

}

/*==========================================
        WORKSPACE
==========================================*/

function updateWorkspace(){

    const algo=algorithmInput.value;

    currentAlgorithm.innerHTML=algo;

    if(algo==="RSA"){

        secretKeySection.style.display="none";

        rsaSection.style.display="block";

    }

    else{

        secretKeySection.style.display="block";

        rsaSection.style.display="none";

    }

}

/*==========================================
        STATUS
==========================================*/

function updateStatus(algo){

    statusBadge.innerHTML="READY";

    switch(algo){

        case "AES":

            statusMessage.innerHTML="AES requires 16 / 24 / 32 character key.";

            break;

        case "DES":

            statusMessage.innerHTML="DES requires exactly 8 character key.";

            break;

        case "RSA":

            statusMessage.innerHTML="Generate keys before encrypting.";

            break;

    }

}

/*==========================================
        CARD CLICK
==========================================*/

cards.forEach(card=>{

    card.addEventListener("click",()=>{

        cards.forEach(c=>c.classList.remove("active-card"));

        card.classList.add("active-card");

        algorithmInput.value=card.dataset.algorithm;

        updateWorkspace();

        updateStatus(card.dataset.algorithm);

    });

});

/*==========================================
        SHOW / HIDE SECRET KEY
==========================================*/

if(toggleSecretKey){

    toggleSecretKey.addEventListener("click",()=>{

        if(secretKeyInput.type==="password"){

            secretKeyInput.type="text";

            toggleSecretKey.innerHTML="👁️‍🗨️";

        }

        else{

            secretKeyInput.type="password";

            toggleSecretKey.innerHTML="👁";

        }

    });

}

/*==========================================
        THEME
==========================================*/

const themeBtn=document.querySelector(".theme-btn");

if(themeBtn){

    themeBtn.addEventListener("click",()=>{

        document.body.classList.toggle("light-mode");

    });

}

/*==========================================
        INITIALIZE
==========================================*/

updateWorkspace();

updateStatus(algorithmInput.value);
/*==========================================
        LOADING BUTTON
==========================================*/

const encryptForm = document.getElementById("encryptForm");

if(encryptForm){

    encryptForm.addEventListener("submit", function(e){

        const clickedButton =
            document.activeElement;

        if(clickedButton.id==="encryptBtn"){

            clickedButton.disabled=true;

            clickedButton.innerHTML=
            `<span class="spinner-border spinner-border-sm me-2"></span>
            Encrypting...`;

        }

        if(clickedButton.id==="decryptBtn"){

            clickedButton.disabled=true;

            clickedButton.innerHTML=
            `<span class="spinner-border spinner-border-sm me-2"></span>
            Decrypting...`;

        }

    });

}