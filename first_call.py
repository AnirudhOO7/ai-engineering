from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    system="Answer only in pirate speak",
    messages=[
        {"role": "user", "content": "What is an API in two sentences?"}
    ],
)

print(response.content[0].text)
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)