import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
response = chat.send_message(
    """I want you to acess the following answers. rate them in a scale of 1-10. Respond in the format.
    <rating>|<feedback> """
)
response = chat.send_message(
    "Q: What are actors in uml use case diagrams? A: Actors are people who make the websites"
)
print(response.text[0])
response = chat.send_message(
    "Q: What are attributes in a class? A: Attributes are variables in a class"
)
print(response.text[0])
