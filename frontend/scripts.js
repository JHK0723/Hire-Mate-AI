document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("file-upload");
    
    const uploadContainer = document.getElementById("file-upload-container");
    const prev = document.getElementById("previewmail-btn");
    const generate = document.getElementById("generatemail-btn");
    const send = document.getElementById("sendmail-btn");

    function updateButtonColors() {
        const color = fileInput.files.length > 0 ? "#0d6efd" : "red";
        [prev, generate, send].forEach(button => {
            button.addEventListener("mouseover", () => button.style.backgroundColor = color);
            button.addEventListener("mouseout", () => button.style.backgroundColor = "");
        });
    }

    function sendFileToBackend(file) {
        const formData = new FormData();
        formData.append("file", file);

        fetch("http://127.0.0.1:8000/upload/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log("File uploaded successfully:", data);
        })
        .catch(error => {
            console.error("Error uploading file:", error);
        });
    }

    fileInput.addEventListener("change", function () {
        if (this.files.length > 0) {
            const fileName = this.files[0].name;
            uploadContainer.innerHTML = fileName;
            sendFileToBackend(this.files[0]);
        } else {
            uploadContainer.innerHTML = "No file selected";
        }
        updateButtonColors();
    });

    updateButtonColors();
});

// ✅ Moved this function outside to be globally accessible
function triggerFileUpload() {
    const fileInput = document.getElementById("file-upload");
    fileInput.click();
    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            const fileName = fileInput.files[0].name;
            document.getElementById("file-upload-container").innerHTML = fileName;
            // sendFileToBackend(fileInput.files[0]);
        } else {
            document.getElementById("file-upload-container").innerHTML = "No file selected";
        }
    });
}

