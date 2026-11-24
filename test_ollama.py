import ollama

print("Connecting to Ollama...")

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": "Say hello as a Business Analyst in one sentence."
        }
    ]
)

print("Response received:")
print(response["message"]["content"])
