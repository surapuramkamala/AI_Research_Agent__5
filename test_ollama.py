import ollama


try:

    print("Testing Ollama...")

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": "Say hello in one sentence."
            }
        ]
    )

    print("\nOLLAMA RESPONSE:")
    print(response["message"]["content"])

except Exception as error:

    print("\nOLLAMA FAILED")
    print(type(error).__name__)
    print(str(error))