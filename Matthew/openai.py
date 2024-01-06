from dotenv import load_dotenv
import openai
import os
from Friday-bot.Matthew.openai import chatgpt_response

load_dotenv()

openai.api_key = os.getenv('API_KEY')

def chat_gpt_response(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=100    
    )

    response_dict = response.get("choice")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response