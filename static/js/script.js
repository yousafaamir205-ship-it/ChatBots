const button = document.getElementById("send-btn");

button.addEventListener("click", function () {

    const input = document.getElementById("user-input");
    const chat = document.getElementById("chat-box");

    if (input.value.trim() === "")
        return;

    chat.innerHTML += `
        <div class="user-message">
            ${input.value}
        </div>
    `;

    input.value = "";

    chat.scrollTop = chat.scrollHeight;
});