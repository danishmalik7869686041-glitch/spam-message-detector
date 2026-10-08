const messageInput = document.getElementById("message");
const checkButton = document.getElementById("checkButton");

const resultBox = document.getElementById("result");
const resultIcon = document.getElementById("resultIcon");
const resultText = document.getElementById("resultText");
const confidenceText = document.getElementById("confidence");

async function checkMessage() {
    const message = messageInput.value.trim();

    if (!message) {
        alert("Please enter a message first.");
        return;
    }

    checkButton.disabled = true;
    checkButton.textContent = "Checking...";

    resultBox.className = "result hidden";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        resultBox.classList.remove("hidden");

        if (data.result === "Spam") {
            resultBox.classList.add("spam");
            resultIcon.textContent = "⚠️";
            resultText.textContent = "Spam Message";
        } else {
            resultBox.classList.add("safe");
            resultIcon.textContent = "✅";
            resultText.textContent = "Not Spam";
        }

        confidenceText.textContent =
            `Model confidence: ${data.confidence}%`;

    } catch (error) {
        console.error("Prediction error:", error);

        alert(
            "Unable to check the message. Please make sure the server is running."
        );

    } finally {
        checkButton.disabled = false;
        checkButton.textContent = "Check Message";
    }
}

function useExample(message) {
    messageInput.value = message;
    messageInput.focus();
}