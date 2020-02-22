import logging
import os
import sys

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
import json
from sugaroid.trainer.trainer import SugaroidTrainer
from sugaroid.brain.brain import Neuron
from sugaroid.config.config import ConfigManager


class Sugaroid:
	def __init__(self):
		self.trainer = None
		self.corpusTrainer = None
		self.cfgmgr = ConfigManager()

		# Create a new chat bot named Charlie
		self.chatbot = ChatBot(
			'Sugaroid',
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

		self.read()



	def init_local_trainers(self):
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
			from sugaroid.trainer.trainer import main as trainer
			# FIXME replace with dynamic traine i.e GUI + CLI
			trainer()
		else:
			if os.path.exists('database.db'):
				print("Database already exists")
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
		neuron = Neuron()


	def prompt_cli(self):
		try:
			response = self.chatbot.get_response(input('@> '))
			return response
		except (KeyboardInterrupt, EOFError):
			sys.exit()
	
	def display_cli(self, response):
		print(response)

	def loop_cli(self):
		while True:
			self.display_cli(self.prompt_cli())


def main():
	sg = Sugaroid()
	sg.loop_cli()


if __name__ == "__main__":
	main()
