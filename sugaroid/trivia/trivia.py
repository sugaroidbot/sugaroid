from random import randint
from sugaroid.trivia.triviadb import db


class SugaroidTrivia:
    def __init__(self):
        self.answer_i = None
        self.random_question_instance = db[randint(0, 50)]

    def ask(self):
        category = self.random_question_instance['category']
        difficulty = self.random_question_instance['difficulty']
        question = self.random_question_instance['question']
        self.answer_i = self.random_question_instance['correct_answer']
        return "Category: {c}\nDifficulty: {d}\n\n{q}".format(c=category, d=difficulty, q=question)

    def answer(self):
        return self.answer_i