import os
import sys

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
import json
from sugaroid.trainer.trainer import SugaroidTrainer


class Sugaroid:
	def __init__(self):

		# Create a new chat bot named Charlie
		self.chatbot = ChatBot('Sugaroid',
			storage_adapter='chatterbot.storage.SQLStorageAdapter',
			logic_adapters=[
				'chatterbot.logic.MathematicalEvaluation',
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

		# initialize the trainer
		self.trainer = ListTrainer(self.chatbot)
		self.corpusTrainer = ChatterBotCorpusTrainer(self.chatbot)

		# initialize with minimum converstion

		self.list_train(conversation)

	def list_train(self, li):
		self.trainer.train(li)

	def read(self):
		if 'train' in sys.argv:
			pass
		else:
			if os.path.exists('database.db'):
				pass
			else:
				st = SugaroidTrainer()
				st.train(self.trainer)

	def write(self):
		raise NotImplementedError

	def corpus(self):
		self.corpusTrainer.train(
			"chatterbot.corpus.english.greetings",
		)

	def invoke_brain(self):
		pass

	def prompt_cli(self):
		response = self.chatbot.get_response(input('@> '))
	
	def display_cli(self,):
		
		print(response)

	def main(self):
		pass







while True:
	try:
		response = chatbot.get_response(input('@> '))
		print(response)
	except(KeyboardInterrupt, EOFError, SystemExit):
		break

if __name__ == "__main__":
	sg = Sugaroid()
	sg.main()

