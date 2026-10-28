from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = "You are a helpful, concise assistant."
messages = []

while True:
    user_input = input("\nYou: ")
    if user_input.strip().lower() in {"quit", "exit"}:
        break

    messages.append({"role": "user", "content": user_input})

    print("Claude: ", end="", flush=True)
    reply = ""
    with client.messages.stream(
        model="claude-haiku-5-5",
        max_tokens=500,
        system=SYSTEM,
        messages=messages,
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            reply += text
        print(stream.get_final_message().usage)
    messages.append({"role": "assistant", "content": reply})
    print()