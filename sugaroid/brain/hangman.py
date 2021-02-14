from sugaroid.brain.constants import HOPE_GAME_WAS_GOOD
from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.ooo import Emotion
from sugaroid.core.base_adapters import SugaroidLogicAdapter
from sugaroid.core.statement import SugaroidStatement

HANGMAN_WORDS = """
abruptly
absurd
abyss
affix
askew
avenue
awkward
axiom
azure
bagpipes
bandwagon
banjo
bayou
beekeeper
bikini
blitz
blizzard
boggle
bookworm
boxcar
boxful
buckaroo
buffalo
buffoon
buxom
buzzard
buzzing
buzzwords
caliph
cobweb
cockiness
croquet
crypt
curacao
cycle
daiquiri
dirndl
disavow
dizzying
duplex
dwarves
embezzle
equip
espionage
euouae
exodus
faking
fishhook
fixable
fjord
flapjack
flopping
fluffiness
flyby
foxglove
frazzled
frizzled
fuchsia
funny
gabby
galaxy
galvanize
gazebo
giaour
gizmo
glowworm
glyph
gnarly
gnostic
gossip
grogginess
haiku
haphazard
hyphen
iatrogenic
icebox
injury
ivory
ivy
jackpot
jaundice
jawbreaker
jaywalk
jazziest
jazzy
jelly
jigsaw
jinx
jiujitsu
jockey
jogging
joking
jovial
joyful
juicy
jukebox
jumbo
kayak
kazoo
keyhole
khaki
kilobyte
kiosk
kitsch
kiwifruit
klutz
knapsack
larynx
lengths
lucky
luxury
lymph
marquis
matrix
megahertz
microwave
mnemonic
mystify
naphtha
nightclub
nowadays
numbskull
nymph
onyx
ovary
oxidize
oxygen
pajama
peekaboo
phlegm
pixel
pizazz
pneumonia
polka
pshaw
psyche
puppy
puzzling
quartz
queue
quips
quixotic
quiz
quizzes
quorum
razzmatazz
rhubarb
rhythm
rickshaw
schnapps
scratch
shiv
snazzy
sphinx
spritz
squawk
staff
strength
strengths
stretch
stronghold
stymied
subway
swivel
syndrome
thriftless
thumbscrew
topaz
transcript
transgress
transplant
triphthong
twelfth
twelfths
unknown
unworthy
unzip
uptown
vaporize
vixen
vodka
voodoo
vortex
voyeurism
walkway
waltz
wave
wavy
waxy
wellspring
wheezy
whiskey
whizzing
whomever
wimpy
witchcraft
wizard
woozy
wristwatch
wyvern
xylophone
yachtsman
yippee
yoked
youthful
yummy
zephyr
zigzag
zigzagging
zilch
zipper
zodiac
""".split(
    "\n"
)[
    1:-1
]
HANGAMaN_MARVEL_WORDS="""
captainamerica 
thor 
hawkeye 
blackwidow 
vision 
thanos 
tonystark 
pepperpotts 
happy 
peterparker 
auntmay 
blackpanther 
nickfury 
hill 
gamora 
groot 
rocketracoon 
starlord 
hulk 
ultron 
bucky 
falcon 
antman 
wasp 
wanda 
jarvis 
edith 
mysterio 
skull 
drstrange
vulture
mj
killmonger
shuri
nebula
captainmarvel
loki
drax
yondu
valkyrie
stanlee
""".split(
    "\n"
)[
    1:-1
]

HANGMAN_STICKFIGURE=["""
    +---+
    |   |
        |
        |
        | 
        |
    =========""","""
    +---+
    |   |
    0   |
        |
        |
        |
    =========""",""" 
    +---+
    |   |
    0   |
    |   |
        |
        |
    ========= ""","""
    +---+
    |   |
    0   |
   /|   |
        |
        |
    ========= ""","""
    +---+
    |   |
    0   |
   /|\  |
        |
        |
    =========""","""
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
    ========= ""","""
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
    ========= 
"""]

def Marvel_fans():
    def Random(wordList):
        wordIndex = random.randint(0,len(wordList) - 1)            
        return wordList[wordIndex]
    def game(HANGMANPICS,missedLetters,correctLetters,secretWord):
        print(HANGMANPICS[len(missedLetters)])
        print()

        print('Missed letters:',end = '')
        for letter in missedLetters:
            print(letter,end ='')
        print()

        blanks ='_' * len(secretWord)

        for i in range(len(secretWord)):            
             if secretWord[i] in correctLetters:
                 blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks:       
            print(letter,end=' ')
        print()
    def Guess(alreadyGuessed):

         while True:

             print('Guess a letter.')
             guess = input()

             guess = guess.lower()

             if len(guess) != 1:

                 print('Please enter a single letter.')

             elif guess in alreadyGuessed:

                 print('You have already guessed that letter. Choose again.')

             elif guess not in 'abcdefghijklmnopqrstuvwxyz':

                 print('Invalid Entry! Please enter a LETTER.')

             else:
                 return guess

    def play_Again():

         print('Do you want to play again?(yes/no)')

         return input().lower().startswith('y')


    print('H A N G M A N')

    missedLetters=''

    correctLetters=''

    secretWord=Random(HANGMAN_MARVEL_WORDS)

    game_done=False


     while True:

         game(HANGMANPICS, missedLetters, correctLetters, secretWord)


         guess = Guess(missedLetters + correctLetters)


         if guess in secretWord:

             correctLetters = correctLetters + guess
             foundAllLetters = True

             for i in range(len(secretWord)):

                 if secretWord[i] not in correctLetters:

                     foundAllLetters = False

                     break

             if foundAllLetters : 

                 print('Yes! The secret word is "' + secretWord + '"! You have won!')

                 game_done = True

         else:

             missedLetters = missedLetters + guess

             if len(missedLetters) == len(HANGMANPICS) - 1:

                 game(HANGMANPICS, missedLetters, correctLetters, secretWord)

                 print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')

                 game_done = True


         if game_done:

             if play_Again():
                 missedLetters=''
                 correctLetters=''
                 game_done=False
                 secretWord=Random(HANMAN_MARVEL_WORDS)

             else:
                break
                
HANGMAN_WIN = [
    "Hurray! You won the game!",
    "Lets celebrate. You deserve the win",
    "You won the hangman game. Congratulations",
]

HANGMAN_LOS = [
    "Sorry, You lost the game!",
    "I am sorry, you lost the game, Maybe try again later",
    "You tried your best, you might have missed by a hairline",
]

HANGMAN_EMOJI = [
    "💜",
    "💚",
    "🖤",
    "💛",
    "💙",
    "🤍",
    "❤️",
]


class Hangman:
    def __init__(self, chatbot):
        """
        Initiate the hangman game.
        :param chatbot: a chatterbot.chatbot instance
        """
        self.word = random_response(HANGMAN_WORDS)
        self.dashes = self.gen_dash()
        self.chatbot = chatbot
        self.chatbot.globals["hangman"]["enabled"] = True
        self.life = 7

    def get_remaining_life(self):
        return self.life

    def gen_dash(self):
        return ["﹏"] * len(self.word)

    def process(self, statement):
        if (self.life == 0) or ("﹏" not in self.dashes):
            return self.game_over()

        processed = str(statement).strip()
        if processed == "":
            return "Please enter a character for me to check it"
        if processed.isspace():
            return "You should enter a character for me to check it properly"
        if processed.isdigit():
            return "Don't expect numbers in this word."
        if len(processed) > 1:
            return "You are supposed to enter only a single character. Try again"
        else:
            changed = False
            for i in range(len(self.word)):
                if self.word[i].lower() == processed.lower():
                    self.dashes[i] = processed.upper()
                    changed = True
            if not changed:
                self.life -= 1
                prefix = "Oops, seems like you missed a letter.\n"
            else:
                prefix = "Okay, you got that one right!.\n"
            if self.life == 0 or ("﹏" not in self.dashes):
                return self.game_over()
            else:
                response = "{prefix}[ {dashes} ] HANGMAN:{figure} Life: {heart}".format(
                    prefix=prefix,
                    dashes=" ".join(self.dashes),
                    figure=HANGMAN_STICKFIGURE[self.life - 1]*self.life,
                    heart=HANGMAN_EMOJI[self.life - 1] * self.life,
                )
            return response

    def get_results(self):
        """
        Generates the results after a series of attempts
        :return: Boolean. True for User Win, False for lost
        """
        if "﹏" in self.dashes:
            return False
        else:
            return True

    def game_over(self):
        """
        Congratulation message as response at the end of the game
        :return:
        """
        self.chatbot.globals["hangman"]["enabled"] = False
        results = self.get_results()
        if results:
            response = random_response(HANGMAN_WIN)
        else:
            response = "{}. The word was {}".format(
                random_response(HANGMAN_LOS), self.word
            )
        return response


class HangmanAdapter(SugaroidLogicAdapter):
    """
    Plays hangman with you
    """

    def can_process(self, statement: SugaroidStatement) -> bool:
        if ("hangman" in statement.words) and ("not" not in statement.words):
            return True
        else:
            return self.chatbot.globals["hangman"]["enabled"]

    def process(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ) -> SugaroidStatement:
        response = None
        confidence = 2.0  # FIXME: Override all other answers
        emotion = Emotion.genie
        if "stop" in statement.words:
            self.chatbot.globals["hangman"]["enabled"] = False
            response = "I am sorry. You quit the game abrubtly. {}".format(
                random_response(HOPE_GAME_WAS_GOOD)
            )
        else:
            if not self.chatbot.globals["hangman"]["enabled"]:
                self.chatbot.globals["hangman"]["class"] = Hangman(self.chatbot)
                response = "[ {dashes} ] Life: {heart}".format(
                    dashes=" ".join(
                        self.chatbot.globals["hangman"]["class"].gen_dash()
                    ),
                    heart=HANGMAN_EMOJI[
                        self.chatbot.globals["hangman"]["class"].get_remaining_life()
                        - 1
                    ]
                    * self.chatbot.globals["hangman"]["class"].get_remaining_life(),
                )
            else:
                response = self.chatbot.globals["hangman"]["class"].process(
                    statement.text
                )

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.set_confidence(confidence)
        selected_statement.set_emotion(emotion)
        return selected_statement
