import ollama

response = ollama.chat(
    model="phi3:mini",
    messages=[
        {
            "role": "user",
            "content": "Explain student stress in 3 lines."
        }
    ]
)

print(response["message"]["content"])