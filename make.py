from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# import openai key from .env file
openai_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_key)

# create schema for function calling
def extract_info(data):
    messages = [
        {"role": "system", "content": f"You are a perfect contents analyzer. Now, you should extract all of questions and its full answers from inputted text. Then, output as json format."},
        {"role": "user", "content": data}
    ]

    # define model
    response = openai_client.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        messages = messages,
        temperature = 0
    )
    print("this is response===>", response.choices[0].message.content)

with open(".\scripts\script1.txt", "r") as file:
    data = file.read()

# extract essential questions and answers
extract_info(data)
