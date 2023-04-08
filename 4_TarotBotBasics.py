"""
To 'design' our tarot bot- let's break down its mechanics, step by step.

1. The user will select the desired tarot spread.
2. The bot will draw the cards and tell the user what the are.
3. The bot will interpret the spread.
4. The user can then ask questions and the bot can continue drawing cards/giving advice.

We'll knock each of these goals out, and have a functioning tarot-reading AI.

"""
# Always put all your module imports right up the top of the script.
import json
import os
import openai
import random
from dotenv import load_dotenv
load_dotenv()  # load variables from .env file
openai.api_key = os.getenv('OPENAI_API_KEY')  # Load the API key from .env
# Load the tarot card data out of MajorArcana.json and store it in tarot_data
with open('MajorArcana.json', 'r') as major_arcana_json: 
    tarot_data = json.load(major_arcana_json)
######################################################################
# 1. The user will select the desired tarot spread

# Let's put a pin in this one for now- 
# For development purposes, let's focus on a simple past/present/future 3-card-spread.
spreadSize = 3 # How many cards will we draw?
spread = []    # This is creating an empty 'list' to fill with the cards we draw.
spreadName = "3-Card Past/Present/Future spread"
######################################################################
# 2. The bot will draw the cards and tell the user what the are.

# We can modify the script from earlier, 'Simple_Tarot.py'

#This function will pull a random card out of tarot_data
def draw_card():
    return random.choice(tarot_data) 

while len(spread) < spreadSize: # While we have less cards in the spread than the size its meant to be,
    cardDrawn = draw_card()['name'] # Draw a card and get its name
    spread.append(cardDrawn) # Add the card we've drawn to the spread list.

######################################################################
# 3. The bot will interpret the spread.

# Here is where it gets interesting. Prompt design is a relativley new field, and we're about to embark on it.
# We need to use the data we have accquired and POST it to our AI API.
# The current 3.5 model has a field for 'system' that can be posted at the start of a conversation. atm, (by openai's own admission) it doesn't do much- but its good practice.
briefing = "Assistant is acting as an AI Tarot reader, and will never break character. Assistant speaks like a wise and mysterious soothsayer."
# Now for our prompt. First we'll reinforce our instructions as to how we want the AI to act.
prompt = briefing+"\n" # '\n' is a line-break character.
# Now let's give it the spread. Remember, we want to change this to support more variations than 3 card spreads in the future, so our prompt has to account for variables:
prompt += "I have requested a " + spreadName + ", and have drawn (in order):\n"
i = 0 # 'i' is a standard variable used to describe an 'i'nteger that 'i'terates through data in a loop.
while i < len(spread):
    prompt += spread[i] # Add the name of each card in our spread to the prompt, one at a time
    prompt += "\n"  # Add a line break, to better format our prompt.
    i += 1 # Increase 'i' by 1, so we move ontop the next card.
prompt += "Please interpret these cards as a " + spreadName
# Lets see the prompt we've created by printing it to the terminal when we run the script.
print(prompt)

# When we prompt OpenAI's chat models, we send the whole conversation each time, to give it conext.
conversation = [
        {
            "role": "system",
            "content": briefing
        },
        {
            "role": "user", 
            "content": prompt
        }
    ]
# Now let's post this prompt to the OpenAI API:
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = conversation
)

# Finally, let's print the AI's response
print("\n"+completion.choices[0].message.content)

# Don't forget to add what the AI just said to the record of the conversation.
conversation.append({
    "role": "assistant",
    "content": completion.choices[0].message.content
    })

######################################################################
# 4. The user can then ask questions and the bot can continue drawing cards/giving advice.

followUp = ""
while followUp.lower() != 'thank you':
    followUp = input("\nAny questions? (or type 'thank you' to exit)\n") # This will prompt the user and accept their input

    conversation.append({
        "role": "user",
        "content": "I have a question about this tarot spread, "+followUp
        })

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation
    )

    print("\n"+completion.choices[0].message.content)

    conversation.append({
        "role": "assistant",
        "content": completion.choices[0].message.content
        })

######################################################################

"""
And there we have it!
There are a few improvements that can be easily made to this program:
    - Functionality for more spreads.
    - Functionality for the minor arcana.
    - Functionality for different tarot traditions (thelema/golden dawn/new age/etc)
    - Functionality for different AI Tarot-reader 'personalities' or 'characters'
    - At the moment, it is possible for the bot to draw the same card more than once.
    - The initial prompt is not very secure, and can easily be broken by insisting the bot break character in further conversation.

Also note that we could've simply prompted the AI it for a 3-card spread and it'd draw the cards itself.
The AI is *good*, but its not infallible.
By controlling as much of the conversation & data that we possibly can, we can maximise our chances of getting the results we want.
Consider the difference in asking chatGPT:
"Give me a 3-card tarot spread."
and
"Interpret a 3-card tarot spread with The Hermit as 'past', The Sun as 'present' and the Magician as 'future'"
The latter prompt provides the AI with more details, and will likely garner better results.
"""