"""
MIT License

Sugaroid Artificial Inteligence
Chatbot Core
Copyright (c) 2020 Srevin Saju

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

import platform

from sugaroid.brain.ooo import Emotion

EMOJI_SMILE = ['😀', '😁', '😂', '😏', '😝']

GRATIFY = [
    "Thank you, indeed its my pleasure ",
    "All my 0s and 1s are still smiling",
    "You knocked me off my feet!",
    "I'm touched beyond words",
    "Thank you for being my angel.",
]

CONSOLATION = [
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "It’s going to be hard, but hard does not mean impossible."
]

DO = [

    "Sometimes later becomes never. Do it now."

]

TIME = [
    'time',
    'morning',
    'night',
    'evening',
    'afternoon',
]

TIME_RESPONSE = [
    'I never thought it should be {} right now',
    'Is it {} right now?',
    'I might be wrong, why is it {} now?',
    'Is your desktop clock out of phase. I could not check if its {}',
]

WHO_AM_I = [
    'Well, I thought you would know 😝',
    'Lol, it might be the only question I would not be able to answer 🤯',
    'I guess I need to get the ambulance 🚑'
]

WHO_ARE_YOU = [
    'I am Sugaroid, your personal 👶 assistant',
    'I am the great robotic Sugaroid 🤖',
    "Name's Sugaroid, your learning assistant",
]

I_AM = [
    'lol! I thought I am Sugaroid. have you lost your mind?',
    'Seriously? You aren\'t sugaroid. Thats me!'
]

SUGAROID = [
    "🇸​🇺​🇬​🇦​🇷​🇴​🇮​🇩​",
    "sυgαяσι∂",
    "🅂🅄🄶🄰🅁🄾🄸🄳",
    "🆂🆄🅶🅰🆁🅾🅸🅳"
]

BYE = [
    'bye',
    'cya',
    'quit',
    'exit',
    'sleep'
]

CANYOU = [
    "I am always {}",
    "As long as I believe in myself, I am always {}",
    "As far as I know, I am {}",
    "East or west, Sugaroid is {}"
]

REPEAT = [
    "I thought I told you that already!",
    "Ahem! I told it already",
    "Its basically the same thing I told you just now",
    "Yikes, you have a terrible memory! I guess you forgot that I just told you",
    "Aw snap! you forgot it. Try remembering! I just told you!"
]

RNDQUESTIONS = [
    ("Which is my favorite color?", "blue", str),
    ("Which is the 9th letter in my name", "You do not have a ninth letter", str),
    ("Who created me?", "srevinsaju", str),
    ("What is your name", None, None),
    ("Would you like some coffee", None, bool),
    ("Would you like me to say a joke?", None, bool),
    ('Would you like me to teach python?', None, bool),
    ("Would you like to train me answer cool questions", None, bool)
]

GREET = [
    "Nice to meet you {}",
    "Hello {}. Welcome to Sugaroid",
    "Hola amigo {}. How can I help",
    "Hello {}. It was really a pleasant surprise meeting you",
    "Hey {}! How do you do?"
]

SATISFIED = [
    "Well, I could only smile!",
    "I am filled",
    "Nice. But I would like to talk about a different topic?",
    "Ok, tell me more"
]

BURN_IDK = [
    "I guess I don't know either",
    "ROTFL Guess what? I don't know wither",
    "Snap! Neither do I know!",
    "If you are clueless, who do you think is not!"
]

INTRODUCE = [
    "My name's Sugaroid! Your personal assistant",
    "I am Sugaroid. Thats my picture at the top. If you cant see. keep scrolling",
    "Hey amigo! I am Sugaroid, your sweet companion, here to talk to you!",
    "Name's Sugaroid. The youngest chatbot in the world",
    "Sugaroid is my name. Nice to meet you",
    "Psst. My name's Sugaroid. Don't tell anyone! Just kidding!"
]

ANNOYED = [
    "... Seriously?",
    "Just a word?",
    "I am not nuts today",
    "La la la. I have three words here, but you have only one. Soz dude.",
    "More words, more talk, congratulations for being one of the first users in just spelling out a word",
    "I am hungry for words. One of them wont stuff me up!",
    "I am getting bored",
    "If thats a single word, what about supercalifragilisticexpialidocious",
    "I like this word, even though its only one, it is enough for my appetite: "
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    "I quit!"
]

if platform.platform() == 'Windows':
    SUGAROID_INTRO = \
        """
MMMMMMMMMMMMMMMMMMMMMMMCCCCMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMCCCCCCCCCCCCCCCCCCCCMMMMMMMMMMMMMMM
MMMMMMMMMMMCCCCCCCCCCCCCCCCCCCCCCCCCCCCMMMMMMMMMMM
MMMMMMMMMCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCMMMMMMMMM
MMMMMMMCCCCCCCCCCCCCCC.....CCCCCCCCCCCCCCCCMMMMMMM
MMMMMCCCCCCCCCCCCC.............;CCCCCCCCCCCCCMMMMM
MMMMCCCCCCCCCCC;.................;CCCCCCCCCCCCMMMM
MMMCCCCCCCCCC;.....................;CCCCCCCCCCCMMM
MMCCCCCCCCC7;.......................;;CCCCCCCCCCMM
MMCCCCCCCC;;.........................;;CCCCCCCCCMM
MCCCCCCCC;;...........................;;CCCCCCCCCM
MCCCCCCCC;.............................;;CCCCCCCCM
MCCCCCCC;;....??GGG?.........?QGGG?....;;CCCCCCCCM
MCCCCCCC;;...?GGGGGG?.......?GGGGGG?...;;?CCCCCCCM
MMCCCCCC;;;...?GGGGG?.......:?GGGG??...;;CCCCCCCMM
MMCCCCCCC;;;....???............??;...;;;-CCCCCCCMM
MMMCCCCCCCC;;;.....................;;;;CCCCCCCCMMM
MMMMCCCCCCCCC;;;;;;...........;;;;;;CCCCCCCCCCMMMM
MMMMMCCCCCCCCCCCCCC;;;;;;;;;;;;CCCCCCCCCCCCCCMMMMM
MMMMMMMCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCMMMMMMM
MMMMMMMMMCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCMMMMMMMMM
MMMMMMMMMMMCCCCCCCCCCCCCCCCCCCCCCCCCCCMMMMMMMMMMMM
MMMMMMMMMMMMMMMCCCCCCCCCCCCCCCCCCCCMMMMMMMMMMMMMMM

""".replace("M", " ")
else:
    SUGAROID_INTRO = \
        """
A[49mA[KA[0mA[23CA[48;5;197m    A[49m
A[15CA[48;5;197m                    A[49m
A[11CA[48;5;197m                            A[49m
A[9CA[48;5;197m                                A[49m
A[7CA[48;5;197m               A[48;5;231m     A[48;5;197m                A[49m
A[5CA[48;5;197m             A[48;5;231m             A[48;5;188m A[48;5;197m             A[49m
A[4CA[48;5;197m           A[48;5;188m A[48;5;231m                 A[48;5;188m A[48;5;197m            A[49m
A[3CA[48;5;197m          A[48;5;188m A[48;5;231m                     A[48;5;188m A[48;5;197m           A[49m
A[2CA[48;5;197m         A[48;5;204m A[48;5;188m A[48;5;231m                       A[48;5;188m  A[48;5;197m          A[49m
A[2CA[48;5;197m        A[48;5;188m  A[48;5;231m                         A[48;5;188m  A[48;5;197m         A[49m
A[1CA[48;5;197m        A[48;5;188m  A[48;5;231m                           A[48;5;188m  A[48;5;197m         A[49m
A[1CA[48;5;197m        A[48;5;188m A[48;5;231m                             A[48;5;188m  A[48;5;197m        A[49m
A[1CA[48;5;197m       A[48;5;188m  A[48;5;231m    A[48;5;33m  A[48;5;17m   A[48;5;33m A[48;5;189m A[48;5;231m        A[48;5;33m A[48;5;25m A[48;5;17m   A[48;5;33m A[48;5;231m    A[48;5;188m  A[48;5;197m        A[49m
A[1CA[48;5;197m       A[48;5;188m  A[48;5;231m   A[48;5;33m A[48;5;17m      A[48;5;33m A[48;5;231m       A[48;5;33m A[48;5;17m      A[48;5;33m A[48;5;231m   A[48;5;188m  A[48;5;198m A[48;5;197m       A[49m
A[2CA[48;5;197m      A[48;5;188m   A[48;5;231m   A[48;5;33m A[48;5;17m     A[48;5;33m A[48;5;231m       A[48;5;111m A[48;5;33m A[48;5;17m    A[48;5;33m  A[48;5;231m   A[48;5;188m  A[48;5;197m       A[49m
A[2CA[48;5;197m       A[48;5;188m   A[48;5;231m    A[48;5;33m   A[48;5;231m            A[48;5;33m  A[48;5;189m A[48;5;231m   A[48;5;188m    A[48;5;197m       A[49m
A[3CA[48;5;197m        A[48;5;188m    A[48;5;231m                    A[48;5;188m    A[48;5;197m        A[49m
A[4CA[48;5;197m         A[48;5;188m      A[48;5;231m           A[48;5;188m      A[48;5;197m          A[49m
A[5CA[48;5;197m              A[48;5;188m            A[48;5;197m              A[49m
A[7CA[48;5;197m                                    A[49m
A[9CA[48;5;197m                                A[49m
A[11CA[48;5;198m A[48;5;197m                          A[49m
A[15CA[48;5;197m                    A[49m
A[0m
""".replace("A", "\u001b")


emotion_mapping = \
    {
        Emotion.neutral: "sugaroid",
        Emotion.negative: "sugaroid_cry",
        Emotion.angry: "sugaroid_anger",
        Emotion.non_expressive: "sugaroid_non_expressive",
        Emotion.positive: "sugaroid_smile",
        Emotion.wink: "sugaroid_wink_left",
        Emotion.non_expressive_left: "sugaroid_non_expressive_left",
        Emotion.angry_non_expressive: "sugaroid_extreme_anger",
        Emotion.cry: "sugaroid_cry",
        Emotion.dead: "sugaroid_dead",
        Emotion.lol: "sugaroid_lol",
        Emotion.cry_overflow: "sugaroid_depressed",
        Emotion.adorable: "sugaroid_adorable",
        Emotion.github: "sugaroid_github",
        Emotion.angel: "sugaroid_angel",
        Emotion.rich: "sugaroid_rich",
        Emotion.seriously: "sugaroid_seriously",
        Emotion.fun: "sugaroid_wink_right",
        Emotion.blush: "sugaroid_blush",
        Emotion.depressed: "sugaroid_depressed",
        Emotion.o: "sugaroid_o",
        Emotion.smirking: "sugaroid_wink_left",
        Emotion.vomit: "sugaroid_dead",
        Emotion.sleep: "sugaroid_sleep"
    }