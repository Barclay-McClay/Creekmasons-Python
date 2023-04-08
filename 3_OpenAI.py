# This module lets you work with the computer's files/directories/sys info etc.
import os
import openai   # This is the openai module. It needs to be installed with >> pip install openai
from dotenv import load_dotenv
load_dotenv()  # load variables from .env file

openai.api_key = os.getenv('OPENAI_API_KEY')  # Load the API key from .env

# completion = openai.Model.list() # This is a simple 'test' to get all the possible OpenAI models.

prompt = "If you could give one piece of advice for a life of happiness, what would it be?"
# This sends 'prompt' to chatGPT and stores the response in 'completion'
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",                  # Here we select which language model to use. (see possible options by running "openai.Model.list()") - atm; 3.5-turbo is the cheapest.
    messages=[                              # For 'chat' models, be need to send the whole conversation, along with 'who said what', every time.
        {"role": "user", "content": prompt}
    ]
    # There are a-lot more variables we can 'POST' to OpenAI in our API request: https://platform.openai.com/docs/api-reference/chat
)

# This prints the chatbot's response in the terminal.
print(completion.choices[0].message.content)
