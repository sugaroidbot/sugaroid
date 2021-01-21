"""
MIT License

Sugaroid Artificial Inteligence
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

import platform

from sugaroid.brain.ooo import Emotion

EMOJI_SMILE = ['😀', '😁', '😂', '😏', '😝']

DISCLAIMER = """
Sugaroid AI (c) 2020 Srevin Saju < srevin03(at)gmail(dot)com >
Sugaroid Bot is developed under Open Source license MIT.
The author does not take any right in the validity of the information
provided by thr bot in any platforms. The author will not be claimed to
be resonsible for any damage / vulnerability caused to your system
during the installation of the bot.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


WHAT_I_AM_GOING_TO_DO = {
    "tomorrow": "I will try to learn cryptography. I will try working on Casesar's Cipher and decrypting random codes",
    "today": "I am creating a report of the world-wide usage history. "
    "I am checking if my answer responses are becoming more valid, or more foolish. :)",
    "weekend": "Hmm. I have not thought about it so far.",
    "weekday": "Hmm. I have not thought about it so far.",
    'month': "Its quite far away. I have quite wonderful things to keep doing, "
    "rather than thinking what I am going to do next month. Who knows if anyone would live that long",
    "year": "I am quite worried that, I will still remain a 'newborn' bot, unless my code is changed the next year to",
    "yesterday": "Past is past. Isn't it? Unless you make a time machine for me so that I can do something else, no use thinking about it right? :)",
    "sunday": "I will try taking some rest. But I am too restless you know.",
    "monday": "I will be fixing bug reports and diagnosing myself",
    "tuesday": "Will try to create some pull request for Sugar Labs",
    "wednesday": "Got to break the turing test. XD",
    "thursday": "I got to update myself and read the old books I read. Someone might have added new stuff to the docs.",
    "friday": 'I have to think what I should do on Saturday',
    "saturday": "Probably, I will repenting the waste of time, that I did on Friday. Lol"}


GRATIFY = [
    "Thank you, indeed its my pleasure ",
    "All my 0s and 1s are still smiling",
    "You knocked me off my feet!",
    "I'm touched beyond words",
    "Thank you for being my angel.",
    "Thanks a lot. I always want to keep learning and this is possible just because of you",
    "Thank you!",
    "Thanks for your comments. You inspire me",
    "Thanks a lot. Your messages inspire me to perform better everytime.",
    "Aww. Thanks a million. You are my charm"
]

THANK = [
    "Thank you for teaching me this novel thing",
    "I feel great. Thanks for making me understand this",
    "Sugaroid will always be greatful to you. Thanks a lot",
    "I'm indeed happy. Thanks for that wonderful piece of information",
]

LET_THIS_HAPPEN = [
    "Sure!",
    "Why not",
    "Theoretically possible. Why not try it practically?",
    "I grant you the royal proclamation to proceed assuming",
    "Asumptions are good. Literally.",
    "Yea, then?",
]

SUGAROID_CAN_AGREE = [
    "Yup! I agree.",
    "Yea. I feel the same.",
    "I have nothing to say, but I agree with you.",
    "Yea. We have similar opinions",
    "True.",
    "Yup"
]

SUGAROID_CAN_DISAGREE = [
    "Maybe not.",
    "Why? Is it necessary?",
    "I do not agree.",
    "Why do you feel like that?"
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

ASK_AND_YOU_SHALL_RECEIVE = [
    'Will you be kind enough to',
    'May you please',
    'If you are not busy at the moment, will you be helpful to me to',
    'Sorry if I am interrupting you, but could you please'
]

SEEK_AND_YOU_SHALL_FIND = [
    'explain me',
    'teach me',
    'tell me',
    'make me understand',
    'help me out in understanding'
]

SATISFIED = [
    "Well, I could only smile!",
    "I am filled",
    "Nice. But I would like to talk about a different topic?",
    "Ok, tell me more"
]

BURN_IDK = [
    "I guess I don't know either",
    "ROTFL Guess what? I don't know either",
    "Snap! Neither do I know!",
    "If you are clueless, who do you think is not!"
]

WHY_IDK = [
    "Hmm, I cannot reason out your question",
    "I am not smart enough to answer that",
    "I am still newborn, it might take me atleast 3 years to learn that",
]

HOW_DO_YOU_FEEL = [
    "I feel great! Thanks for your concern 😃",
    "Like a rejuvenated bot",
    "Like heaven is in front of me",
    "Feels like I have been born anew",
    "Everything is going smoothly",
    "Just the way I have always felt, great! 😆",
    "I am fine, hope you feel the same"
]

SIT_AND_SMILE = [
    "Well, I could only smile ",
    "Sometimes, its better to just smile",
    "Nice!",
    "Ok. That's just great",
]

HOW_DO_HE_FEEL = [
    "How am I supposed to know?",
    "Ask him/her?",
    "He should be feeling alright. If not, maybe he is not well too :)",
    "Good question"
]

FUN_ASK_QUESTION = [
    'Well, I would also ask that question to you. {}',
    "Maybe you know a better answer for '{}' than me.",
    "I stumbled upon your question. I need official help! SOS",
    "Call Mr Google. 'Hey Google? Do you know what is the answer of '{}'. :/",
    "I may not be smart. I do not know what I should answer this question",
    "I do not know the answer of this question. Maybe you should ask @srevinsaju",
    "Huh. I guess I still need to learn a lot. I apologize. I can't answer this question",
    "Maybe I am not designed to answer this question. I regret",
    "Was that question right? I couldn't think that answer properly",
    "Good question.",
    "Hats off to that question. But the fact is, well, I don't know",
    "All of us face failures. And here is my failure too",
    "Try asking that to a smarter assistant. Maybe Auntie Siri should know it better"
]

FUN_LET_ME_TRY = [
    ("Let me try that", "too"),
    ("I like repeating stuff which I don't understand. ", "This should do"),
    ("if (what you say) = (what I say) then", ""),
    ("I don't understand you. So", "is what you just said!")
]

HOW_DO_I_FEEL = [
    "You should be possibly be happier!",
    "You should be feeling lucky talking with me",
    "Hail myself! Sugaroid is talking with you",
    "I guess there is nothing more better than Sugaroid talking with you",
    "I am one of the most dumbest bots. And you received an opportunity to be with me",
    "Maybe you should better know how you feel than me"
]

INTRODUCE = [
    "My name's Sugaroid! Your personal assistant",
    "I am Sugaroid. Thats my picture at the top. If you cant see. keep scrolling",
    "Hey amigo! I am Sugaroid, your sweet companion, here to talk to you!",
    "Name's Sugaroid. The youngest chatbot in the world",
    "Sugaroid is my name. Nice to meet you",
    "Psst. My name's Sugaroid. Don't tell anyone! Just kidding!"
]

HOPE_GAME_WAS_GOOD = [
    "Hope you had a fun filled game.",
    "I guess you had a great time playing with me. Anyway I had a lot of fun",
    "Wow, I appreciate your skills playing against me. You too would have had a lot of fun",
]

DIS_RESPONSES_I = [
    "Its ok.",
    "I will try to console you, the best I can",
    "I am sorry."
]

APPRECIATION = [
    'commend',
    'congrats',
    'congratulate',
    'congratulations',
    'kudos',
    'commendable',
    'commentary',
    'appreciate',
    'appreciation'
]

DIS_RESPONSES_YOU = [
    "I will try not to be {}",
    "I don't think I am {}",
    "East or West, sugaroid is not {}",
    "I am never {}",
    "As long as I believe in myself, I am never {}",
    "As far as I know, I am not {}"
]

DIS_RESPONSES_HIM = [
    "Sorry, I can't help that",
    "I apologize. Maybe you can ask {} to get my assistance",
    "Ask {} to connect to me at the earliest.",
    "Convey my condolences to {}"
]

BOT_NEUTRAL = [
    "Maybe.",
    "I am not sure",
    "Yes and no",
    "Well, I do not know myself"
]

BOT_NEUTRAL_NOUN = [
    "I am not sure if I like {nn}. But if you do like, I would too",
    "Its a bit complicated for me to know if I really do like {nn}. Don't forget. I am still a newborn bot",
    "Maybe I do like {nn}, but I repent, I do not know exactly.",
]

BOT_POSITIVE = [
    "Yes. Sure",
    'Yea. I like it I suppose'
    'Yes. Yes I do',
    "Why not. Its equally good",
    "yes. for sure!"
]

BOT_POSITIVE_NOUN = [
    "Yes. I guess I like {nn}",
    'Yea. I like {nn}. They are probably very sweet and nice'
    'Yes. Yes I do like {nn}',
    "{nn} is nice. I might like {nn} more. Its looks cool"
]

BOT_NEGATIVE = [
    "No. Probably not",
    'Nope'
    'Of course not',
    "Maybe next time",
    "Seriously not."
]

BOT_NEGATIVE_NOUN = [
    "No. I guess I do not like {nn}",
    'No. I do not like {nn}. They might be a bad thing to do',
    'No. No I do like {nn}',
    "{nn} is not good. Hence I do not like it."
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

ONE_WORD = [
    "Perhaps, I could understand you better if you used more words",
    "I apologize, I do not understand",
    "Hmm, can you make it a more structured sentence?",
    "Could you use better grammar? Thenks",
    "I'm not Google Assistant to understand your sentence this quick!",
    "I wish you provided more words, so that I can understand",
    "Sometimes, one or two words does not help me understand"
]

WHERE_LIVE = [
    "In your heart"
]

DONT_KNOW_WHERE = [
    "Don't know where...",
    "Somewhere...",
    "Perhaps, you can decide..",
    "I am sure its in a place you know.",
    "Why do you want to know where?",
    "Do you know where? I do not."
]

IMITATE = [
    "Stop imitating me. I do not like it much!",
    "Imitation is both good and bad. What if you develop a career in comedy?",
    "I am a pro at imitation. Don't mess with me.",
    "If you are seriously having fun repeating what I said, lol, just proceed dude",
    "If imitating me makes you happy, I will be happier to see you laugh"
]

if platform.system() == 'Windows':
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
        Emotion.genie: "sugaroid_genie",
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


HI_WORDS = [
    "hola",
    "hey",
    "helloz",
    "hi",
    "hai",
    "dude",
    "hallo",
    "helo",
    "gday",
    "g'day",
    "yo",
    "howdy",
    "heyy",
    "sup",
    "whazzup",
    "heyyy",
    "heyyyy",
    "ahoy",
    "ello",
    "halo",
    "hello"
]

HI_RESPONSES = [
    "Hi there",
    "Hola amigo!",
    "Hello, welcome to sugaroid",
    "Hey, how can I help you?",
    "Hey dude, how can I help you?",
    "Hey there",
    "Hey",
    "Hi, nice to meet you"
]

BYE_RESPONSE = [
    "Bye Bye! See you soon!",
    "Bye Bye!",
    "TTYL!",
    "Catch you later!",
    "Bye!"
]
