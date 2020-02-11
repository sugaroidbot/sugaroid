from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot


# Create a new chat bot named Charlie
chatbot = ChatBot('Sugaroid')
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatterbot.trainers.UbuntuCorpusTrainer(chatbot)
corpusTrainer = ChatterBotCorpusTrainer(chatbot)
corpusTrainer.train(
    "chatterbot.corpus.english.greetings",
)

trainer = ListTrainer(
    chatbot,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        {
          'import_path': 'chatterbot.logic.BestMatch',
          'default_response': 'I am sorry, but I do not understand.',
          'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.db',
    preprocessors = ['chatterbot.preprocessors.clean_whitespace',
                     'chatterbot.preprocessors.convert_to_ascii'
    ]
  )


trainer.train(conversation)


while True:
    try:
        response = chatbot.get_response(input('@> '))
        print(response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break