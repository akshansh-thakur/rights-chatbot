async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const message = inputField.value.trim();

    
    if (message === "") return;

    addMessage(message, "user");
    inputField.value = "";

    // Add typing indicator
    const typingDiv = addTyping();

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Remove typing indicator
    typingDiv.remove();

    addMessage(data.reply, "bot");
}

function sendIndiaHelplines() {
    quickSend("Show India emergency helplines");
}


function quickSend(text) {
    document.getElementById("user-input").value = text;
    sendMessage();
}


function addMessage(text, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message", sender);
    messageDiv.innerText = text;

    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addTyping() {
    const chatBox = document.getElementById("chat-box");

    const typingDiv = document.createElement("div");
    typingDiv.classList.add("typing");

    typingDiv.innerHTML = `
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
    `;

    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    return typingDiv;
}

