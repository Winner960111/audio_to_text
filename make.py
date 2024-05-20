from openai import OpenAI
from openpyxl import Workbook
from dotenv import load_dotenv
import os
import json
load_dotenv()

# import openai key from .env file
openai_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_key)

workbook = Workbook()
sheet = workbook.active
# create schema for function calling
def extract_info(data):
    print("I'm here")
    extract_info = [
    {
        "type": "function",
        "function": {
            "name": "extract_info",
            "description": "Extract all questions and its answers from inputted text.",
            "parameters":{
                "type": "object",
                "properties": {
                    "QA":{
                        "type":"array",
                        "items":{
                            "type":"object",
                            "properties":{
                                "question":{
                                    "type":"string",
                                    "description": "Extract question from the inputted text."
                                },
                                "answer": {
                                    "type": "string",
                                    "description": "Extract answer about above qestion from the inputted text."
                                }
                            }
                        }
                    }
                },
                "required": ["QA", "question", "answer"]
            }
        }
    }
]
    messages = [
        {"role": "system", "content": f"You are a perfect contents analyzer. Now, you should extract all of questions and its answers from inputted text."},
        {"role": "user", "content": data}
    ]

    response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=0,
                tools=extract_info,
            )
    return response.choices[0].message.tool_calls[0].function.arguments

for category in range(17,400):
    with open(f".\scripts\script{category}.txt", "r") as file:
        data = file.read()
        print("\n data===>",data[:10])
    with open(".\output.json", "r") as file:
        name = file.read()

    # extract essential questions and answers
    
    while True:
        try:
            temp_result = extract_info(data)
            print("\nthis is result===>",temp_result)

            result = json.loads(temp_result)

            append_list = [json.loads(name)[category]['music_name']]
            for item in range(0, len(result['QA'])):
                append_list.append(result['QA'][item]['question'])
                append_list.append(result['QA'][item]['answer'])

            break
        except Exception as e:
            print("re_attempt===>",e)
            pass

    sheet.append(append_list)
    workbook.save("result.xlsx")
    print("step is ===>", category)
