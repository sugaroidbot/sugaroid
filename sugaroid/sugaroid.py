from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot

class Sugaroid:
    pass


# Create a new chat bot named Charlie
chatbot = ChatBot('Sugaroid',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                    
                      {
                          'import_path': 'chatterbot.logic.BestMatch', 
                          'default_response': 'I am sorry, but I do not understand.',
                          'maximum_similarity_threshold': 0.90
                      },

                  ],
                  database_uri='sqlite:///database.db',
                  )
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

import json
with open('trainer.json', 'r') as r:
    data = json.load(r)


corpusTrainer = ChatterBotCorpusTrainer(chatbot)
corpusTrainer.train(
    "chatterbot.corpus.english.greetings",
)

trainer = ListTrainer(chatbot)
print(data)
for i in data:
    print("training", i)
    trainer.train(data[i])
trainer.train(conversation)


while True:
    try:
        response = chatbot.get_response(input('@> '))
        print(response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

