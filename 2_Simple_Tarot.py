# This is a simple python script which will draw a random tarot card, and display some simple interpretations of it.
# There is another file in this directory called 'major-arcana.json'. It stores all the major-arcana tarot cards in a codified way.

# Python loads-up with basic functionality, but for more complex projects- you'll need to import modules to introduce extra functionality.
# 'import' is used to bring external 'packages' or 'modules' into your script.
import random
# 'random' is a module that is used for generating random numbers. We'll be using it for this project.

# Aside from 'random', we also need the 'json' module, to read and properly handle the tarot card data we have stored in another file.
import json

# We are going to open the 'major-arcana.json' file in 'read' ('r') mode, and store the file in a variable 'major_arcana_json'
# Then we convert the json data into a Python-friendly array with json.load, and store that array in a variable named 'tarot_data'.
with open('major-arcana.json', 'r') as major_arcana_json: 
    tarot_data = json.load(major_arcana_json)

# Let's *def*ine 'drawing a tarot card' as a function that we can use and re-use.
def draw_card():
    # We'll use the 'random.choice()' method from the 'random' module we imported, to pick a random object out of 'tarot_data' and store it in 'chosen_card'
    chosen_card = random.choice(tarot_data)
    # Now we'll print the name and interpretation of the chosen_card to the terminal.
    print(chosen_card['name'])
    print(chosen_card['interpretation'])

# Cool. We can draw a random tarot card simply by typing 'draw_card()'
# Let's do a 3-card-spread. But let's do it with some simple looping just for demonstrative purposes:
count = 1 
while count < 4:
    print("Card "+str(count))
    draw_card()
    count += 1
# When you run this code, it will draw three tarot cards, as 'Card 1... Card 2... Card 3...' and give you their name & interpretation.