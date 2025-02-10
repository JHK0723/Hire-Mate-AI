document.addEventListener("DOMContentLoaded", function() {
    
     fetch("http://127.0.0.1:8080/preview/")
        .then(response => response.json())
        .then(data => {
            console.log("Response received:", data);
            document.getElementById("previewmail").innerHTML = `<pre>${data.message1}</pre>`;
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            document.getElementById("data").innerText = "Failed to load data!";
        });
});


// function generatemail() {
//     console.log("Button clicked, showing loading screen...");

//     // Show loading screen
//     document.getElementById("loading-screen").style.display = "flex";

//     fetch("http://127.0.0.1:8000/")
//         .then(response => response.json())
//         .then(data => {
//             console.log("Response received:", data);
//             document.getElementById("generatemail").innerHTML = `<pre>${data.message1}</pre>`;
//             document.getElementById("loading-screen").style.display = "none";
//         })
//         .catch(error => {
//             console.error("Error fetching data:", error);
//             document.getElementById("data").innerText = "Failed to load data!";
//             document.getElementById("loading-screen").style.display = "none"; // Hide loader on error
//         });