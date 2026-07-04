const button = document.getElementById("send-btn");
const input = document.getElementById("user-input");
const chat = document.getElementById("chat-box");
const teachBox = document.getElementById("teach-box");
const answerInput = document.getElementById("answer-input");
const topicInput = document.getElementById("topic-input");
const teachButton = document.getElementById("teach-btn");

let lastQuestion = "";
function saveChat() {
    localStorage.setItem("chatHistory", chat.innerHTML);
}
async function sendMessage() {

    const message = input.value.trim();

    if (message === "")
        return;

    chat.innerHTML += `
    <div class="user-message">
        ${message}
    </div>
`;

saveChat();
    


    input.value = "";

    chat.scrollTop = chat.scrollHeight;

    const typing = document.createElement("div");
    typing.className = "bot-message";
    typing.id = "typing";
    typing.innerHTML = "YChatBot is typing...";

    chat.appendChild(typing);

    chat.scrollTop = chat.scrollHeight;
    await new Promise(resolve => setTimeout(resolve, 1000));
    lastQuestion = message;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();
    if (!data.known) {
    teachBox.style.display = "block";
    }
    else {
    teachBox.style.display = "none";
    }

    document.getElementById("typing").remove();

    chat.innerHTML += `
        <div class="bot-message">
            ${data.reply}
        </div>
        
    `;
    saveChat();

    chat.scrollTop = chat.scrollHeight;
}

button.addEventListener("click", sendMessage);

input.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
window.onload = function () {

    const history = localStorage.getItem("chatHistory");

    if (history) {
        chat.innerHTML = history;
        chat.scrollTop = chat.scrollHeight;
    }

    input.focus();
};
teachButton.addEventListener("click", async function () {

    const answer = answerInput.value.trim();
    const topic = topicInput.value.trim();

    if (answer === "" || topic === "") {
        alert("Please fill in both fields.");
        return;
    }

    await fetch("/teach", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: lastQuestion,
            answer: answer,
            topic: topic
        })
    });

    chat.innerHTML += `
        <div class="bot-message">
            ✅ Thank you! I learned something new.
        </div>
    `;

    saveChat();

    teachBox.style.display = "none";

    answerInput.value = "";
    topicInput.value = "";

});