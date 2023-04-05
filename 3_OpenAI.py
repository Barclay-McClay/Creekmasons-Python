import os       # This module lets you work with the computer's files/directories/sys info etc.
import openai   # This is the openai module. It needs to be installed with >> pip install openai
from dotenv import load_dotenv 
load_dotenv()  # load variables from .env file

openai.organization = " "
openai.api_key = " "

response = openai.Model.list()
print(response)