import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

for text in ["hello", "Hello world!", "unbelievable", "supercalifragilistic", "नमस्ते", "12345678"]:
    tokens = enc.encode(text)
    print(f"{text!r}: {len(tokens)} tokens -> {[enc.decode([t]) for t in tokens]}")