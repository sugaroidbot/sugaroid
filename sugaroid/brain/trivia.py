"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020-2021 Srevin Saju
Copyright (c) 2021 The Sugaroid Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.trivia.trivia import SugaroidTrivia


class TriviaAdapter(LogicAdapter):
    """
    Plays a short game of trivia
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.cos = None

    def can_process(self, statement):
        self.cos = max([
            self.chatbot.lp.similarity(str(statement), 'Ask ne a question'),
            self.chatbot.lp.similarity(
                str(statement), 'Lets have some trivia'),
            self.chatbot.lp.similarity(str(statement), 'Play trivia'),
            self.chatbot.lp.similarity(
                str(statement), 'Can you ask some quiz'),
            self.chatbot.lp.similarity(str(statement), 'Can you quiz'),
            self.chatbot.lp.similarity(str(statement), 'Can you play trivia'),
        ])
        if self.cos > 0.9:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        st = SugaroidTrivia()
        response = st.ask()
        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = self.cos
        self.chatbot.globals['trivia_answer'] = st.answer()
        emotion = Emotion.neutral
        selected_statement.emotion = emotion
        return selected_statement
