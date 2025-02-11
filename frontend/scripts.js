document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("file-upload");
    const submitButton = document.getElementById("file-upload-container");
    const prev = document.getElementById("previewmail-btn");
    const generate = document.getElementById("generatemail-btn");
    const send = document.getElementById("sendmail-btn");

    function sendFileToBackend(file) {
        console.log("Button clicked, showing loading screen...");
        const formData = new FormData();
        formData.append("file", file);
        console.log("Sending file to backend:", file.name);

        fetch("http://127.0.0.1:8080/upload/", {
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

    function triggerFileUpload() {
        fileInput.click();
    }

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            const fileName = fileInput.files[0].name;
            submitButton.innerHTML = fileName;
        } else {
            submitButton.innerHTML = "No file selected";
        }
    });

    function submitbutton() {
        if (fileInput.files.length > 0) {
            sendFileToBackend(fileInput.files[0]);
        } else {
            alert("Please upload a file before submitting.");
        }
    }

    // Assign the functions to global scope for button clicks
    window.triggerFileUpload = triggerFileUpload;
    window.submitbutton = submitbutton;
    document.getElementById("send-email-btn").addEventListener("click", async () => {
        try {
            const response = await fetch("http://127.0.0.1:8080/send-emails/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            });

            const data = await response.json();
            console.log("Email sending bg") // Show confirmation message
        } catch (error) {
            console.error("Error sending email:", error);
            alert("Failed to send email.");
        }
    });
    
});
