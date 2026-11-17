
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

# Initialize Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Create conversation
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

print("\n===== RAHUL AI CHATBOT =====")
print("Ask anything. Type 'exit' to stop.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot closed!")
        break

    try:
        response = chat.send_message(user_input)

        print("\nGemini:", response.text)
        print()

    except Exception as e:
        print("\nError:", e)
