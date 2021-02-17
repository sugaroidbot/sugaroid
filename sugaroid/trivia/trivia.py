from random import shuffle

import requests



class SugaroidTrivia:
    """
    Prepares a sugaroid trivia database to ask the users
    some random questions from the trivia db.

    This can be used as

        >>> strivia = SugaroidTrivia()
        >>> print(strivia.ask())
        >>> # get the answer
        >>> strivia.ch()

    """

    def __init__(self):
        self.answer_i = None
        self._correct_answer_idx = 0

        response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
        self._response = response.json()

        # results parsed
        results = self._response["results"][0]
        self.category = results["category"]
        self.difficulty = results["difficulty"]
        self.question = results["question"]
        self.correct_answer = results["correct_answer"]
        self.incorrect_answers = results["incorrect_answers"]
        self._options = None

    def ask(self) -> str:
        options = [self.correct_answer] + self.incorrect_answers
        shuffle(options)

        self._correct_answer_idx = options.index(self.correct_answer)
        self._options = options
        return """Difficulty: {difficulty}
        
Q: {question}

Options
a. {option_a}
b. {option_b}
c. {option_c}
d. {option_d}""".format(difficulty=self.difficulty, question=self.question,
                   option_a=options[0], option_b=options[1], option_c=options[2], option_d=options[3])

    def check_answer(self, answer: str) -> bool:
        if answer.strip().isdigit():
            is_correct = answer.strip().isdigit() == str(self._correct_answer_idx)
        else:
            is_correct = answer.strip() == self.correct_answer
        return is_correct

