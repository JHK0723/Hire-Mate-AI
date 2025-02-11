const fileInput = document.getElementById("file-upload");
console.log(fileInput.files.length);
function triggerFileUpload() {
    fileInput.click();
    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            const fileName = fileInput.files[0].name;
            document.getElementById("file-upload-container").innerHTML = fileName;
        } else {
            document.getElementById("file-upload-container").innerHTML = "No file selected";
        }
    });
}
function sendFileToBackend(file) {
    const formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:8080/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log("File uploaded successfully:", data);
        // Handle success response
    })
    .catch(error => {
        console.error("Error uploading file:", error);
        // Handle error response
    });
}
// unused function
document.getElementById("file-upload").addEventListener("change", function () {
    const fileName = this.files.length > 0 ? this.files[0].name : "No file selected";
    document.getElementById("file-name").textContent = fileName;
});
function generatemail() {
    console.log("Button clicked, showing loading screen...");

    // Show loading screen
    document.getElementById("loading-screen").style.display = "flex";

    fetch("http://127.0.0.1:8080/")
        .then(response => response.json())
        .then(data => {
            console.log("Response received:", data);
            document.getElementById("generatemail").innerHTML = `<pre>${data.message1}</pre>`;
            document.getElementById("loading-screen").style.display = "none";
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            document.getElementById("data").innerText = "Failed to load data!";
            document.getElementById("loading-screen").style.display = "none"; // Hide loader on error
        });
}
function previewmail() {
    window.location.href = "http://127.0.0.1:5501/preview.html";
}





function sendmail(){
    document.getElementById("sendmail").innerHTML = "<p class='fadein'>Mail Sent!</p>";
}

const prev = document.getElementById("previewmail-btn");
const generate = document.getElementById("generatemail-btn");
const send = document.getElementById("sendmail-btn");
fileInput.addEventListener("change", updateButtonColors);
function updateButtonColors(){
 if (fileInput.files.length == 0) {
    prev.addEventListener("mouseover", function() {
        prev.style.backgroundColor = "red";
    });
    prev.addEventListener("mouseout", function() {
        prev.style.backgroundColor = "";
    });
    generate.addEventListener("mouseover", function() {
        generate.style.backgroundColor = "red";
    });
    generate.addEventListener("mouseout", function() {
        generate.style.backgroundColor = "";
    }  );
    send.addEventListener("mouseover", function() {
        send.style.backgroundColor = "red";
    });
    send.addEventListener("mouseout", function() {
        send.style.backgroundColor = "";
    });
 }
 else{
    prev.addEventListener("mouseover", function() {
        prev.style.backgroundColor = "#0d6efd";
    });
    prev.addEventListener("mouseout", function() {
        prev.style.backgroundColor = "";
    });
    generate.addEventListener("mouseover", function() {
        generate.style.backgroundColor = "#0d6efd";
    });
    generate.addEventListener("mouseout", function() {
        generate.style.backgroundColor = "";
    }  );
    send.addEventListener("mouseover", function() {
        send.style.backgroundColor = "#0d6efd";
    });
    send.addEventListener("mouseout", function() {
        send.style.backgroundColor = "";
    });
 }
}
updateButtonColors();