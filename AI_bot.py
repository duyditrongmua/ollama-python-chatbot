from openai import OpenAI
client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama"
)
message = []

while True:
    print(message)
    user_input = input("You: ")
    if user_input == "exit":
        break
    message.append({"role": "user", "content": user_input})
    respond = client.chat.completions.create(
        model="gemma3:1b",
        stream = True,
        messages = message
    )

    bot_reply = ""
    for chunk in respond:
        bot_reply += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "", end = "", flush = True)
    message.append({"role": "assistant", "content": bot_reply})