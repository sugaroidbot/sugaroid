import logging
import os
import sys

import logging

logging.basicConfig(level=logging.INFO)

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
		self.neuron = None
		self.cfgmgr = ConfigManager()
		self.cfgpath = self.cfgmgr.get_cfgpath()
		self.database_exists = os.path.exists(os.path.join(self.cfgpath, 'sugaroid.db'))

		# Create a new chat bot named Charlie
		self.chatbot = ChatBot(
			'Sugaroid',
			storage_adapter='chatterbot.storage.SQLStorageAdapter',
			logic_adapters=[
				'chatterbot.logic.MathematicalEvaluation',
				{
					'import_path': 'chatterbot.logic.BestMatch',
					'default_response': 'I am sorry, but I do not understand.',
					'maximum_similarity_threshold': 0.80
				}
			],
			database_uri='sqlite+pysqlite:///{}/sugaroid.db'.format(self.cfgpath),
		)
		self.read()
		self.invoke_brain()

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
			if self.database_exists:
				print("Database already exists")
				pass
			else:
				if self.trainer is None:
					self.init_local_trainers()

				st = SugaroidTrainer()
				st.train(self.trainer)

	def write(self):
		raise NotImplementedError

	def corpus(self):
		self.corpusTrainer.train(
			"chatterbot.corpus.english.greetings",
		)

	def invoke_brain(self):
		self.neuron = Neuron(self.chatbot)

	def prompt_cli(self):
		try:
			response = self.neuron.parse(input('@> '))
			return response
		except (KeyboardInterrupt, EOFError):
			sys.exit()

	@staticmethod
	def display_cli(response):
		print(response)

	def loop_cli(self):
		while True:
			self.display_cli(self.prompt_cli())


def main():
	sg = Sugaroid()
	sg.loop_cli()


if __name__ == "__main__":
	main()
