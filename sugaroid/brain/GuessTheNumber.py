import random
from sugaroid.brain.constants import HOPE_GAME_WAS_GOOD
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.ooo import Emotion
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement

GUESS_NUM_WIN = [
"Congragulations! You really are a genius.",
"You havae won the game by Guessing the Number correctly.",
"Let the celebrations begin!",
]

GUESS_NUM_LOS = [
"That was close.",
"Better Luck Next Time Mate.",
"Be enthusiastic and give it a try once more!',
]

GUESS_NUM_EMOJI = [
    "🤍",
    "💜",
    "💙",
    "💚",
    "💛",
    "🧡",
    "🤎",
    "🖤",
    "❤️",
]

class GUESS_GAME:
    def __init__(self,chatbot):
        """
        Initiate the guess the number game.
        :param chatbot: a chatterbot.chatbot instance
        """
        self.num = random.randint(1,100)
        self.chatbot = chatbot
        self.chatbot.globals["guessthenumber"]["enabled"] = True
        self.life = 9
        
    def remaining_life(self):
        return self.life
        
    def game(self,statement):
        if self.life == 0:
            return self.game_over()
            
        processed = str(statement).strip()
        if processsed == "":
            return "Please enter a number for me to check it!"
        if processed.isspace():
            return "You should enter  for me to check it!"
        if process.isalpha():
            return "There are no aplhabets in the number. Please enter a nuumber!"
        
        
        
        
        
        
        
        
        
