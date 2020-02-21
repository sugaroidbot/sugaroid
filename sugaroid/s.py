from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create a new instance of a ChatBot
bot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(bot)

# Train the chat bot with a few responses

import json
with open('trainer.json', 'r') as r:
    data = json.loads(r.read())

# Get a response for some unexpected input
response = bot.get_response('How do I make an omelette?')
print(response)
# Get a few responses from the bot

print(bot.get_response('What time is it?'))

print(bot.get_response('What is 7 plus 7?'))
