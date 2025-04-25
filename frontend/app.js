const userForm = document.getElementById("userForm");
const usernameInput = document.getElementById("username");
const cityInput = document.getElementById("city");
const greetingMessage = document.getElementById("greeting");
const resultsDiv = document.getElementById("results");
const video = document.getElementById("video");
const preview = document.getElementById("preview");

let capturedImageDataURL = "";

// Start the webcam
async function startWebcam() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
    } catch (error) {
        console.error("Camera access error:", error);
        alert("Unable to access camera. Check permissions.");
    }
}

// Capture image from webcam
function captureImage() {
    const canvas = document.createElement("canvas");
    canvas.width = 224;
    canvas.height = 224;
    const context = canvas.getContext("2d");
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    capturedImageDataURL = canvas.toDataURL("image/jpeg");
    preview.src = capturedImageDataURL;

    // Stop camera
    const stream = video.srcObject;
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        video.srcObject = null;
    }
}

// Call it on load
startWebcam();

// Handle form submission
userForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const username = usernameInput.value.trim();
    const city = cityInput.value.trim();

    if (!username || !city || !capturedImageDataURL) {
        alert("Please enter your name, city, and capture your image!");
        return;
    }

    greetingMessage.textContent = `Hello, ${username.toUpperCase()}! Welcome to the sky page!`;
    console.log("Form submitted. Sending to backend...");

    const payload = {
        city: city,
        image: capturedImageDataURL,
        timestamp: new Date().toISOString()
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("Prediction API failed");

        const data = await response.json();

        resultsDiv.innerHTML = `
            <h3>Results 🌈</h3>
            <p><strong>Skin Type:</strong> ${data.skin_type}</p>
            <p><strong>Confidence:</strong> ${data.confidence}%</p>
            <p><strong>Suggestions:</strong></p>
            <ul>${Array.isArray(data.derma_advice)
                ? data.derma_advice.map(tip => `<li>${tip}</li>`).join("")
                : `<li>${data.derma_advice}</li>`}
            </ul>
        `;
        resultsDiv.style.display = "block";

    } catch (error) {
        console.error("Error during fetch:", error);
        resultsDiv.innerHTML = "<p style='color: red;'>Failed to fetch predictions. Is the backend running?</p>";
        resultsDiv.style.display = "block";
    }
});
