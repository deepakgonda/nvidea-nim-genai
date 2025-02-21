import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("NVIDIA_API_KEY")

# Set up OpenAI client for NVIDIA API
client = openai.OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY
)

def chat_with_ai():
    print("💬 NVIDIA GenAI Chatbot (Type 'exit' to stop)\n")
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break

        chat_history.append({"role": "user", "content": user_input})

        # Call NVIDIA API
        response = client.chat.completions.create(
            model="nvidia/mistral-nemo-minitron-8b-8k-instruct",
            messages=chat_history,
            temperature=0.7,
            max_tokens=150
        )

        reply = response.choices[0].message.content.strip()
        print(f"NVIDIA AI: {reply}\n")

        chat_history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat_with_ai()
