import platform

from sugaroid.brain.ooo import Emotion
from datetime import datetime

BIRTHDAY = datetime(year=2020, month=2, day=11, hour=14, minute=58, second=38)
DATE_STRFTIME = "%A, %B %d, %Y at %H:%M:%S"

EMOJI_SMILE = ["😀", "😁", "😂", "😏", "😝"]

LICENSE = lic = DISCLAIMER = """<pre><code>
MIT License
Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020-2021 Srevin Saju
Copyright (c) 2021 The Sugaroid Project

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above 
copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.</code></pre> """

CREDITS = [
    "<b>The Sugaroid Project</b>, and contributors",
    "<b>Wolfram Alpha</b> for Mathematical evaluation and logical" " wh-questions",
    "<b>The SwagLyrics Project</b>, for the awesome lyrics fetching library",
    "<b>The NewsAPI Project</b>, for the news headlines",
    "<b>Wikipedia</b>, The Free Encyclopedia, by The Wikimedia Foundation",
]

WHAT_I_AM_GOING_TO_DO = {
    "tomorrow": "I will try to learn cryptography. I will first try working on "
    "Casesar's Cipher and decrypting random codes",
    "today": [
        "I am creating a report of the world-wide usage history",
        "I am checking if my responses are becoming more valid, or more foolish😝",
    ],
    "weekend": "I might do some intense training to increase the validity of my responses",
    "weekday": "I guess goofing around once in a while is not such a bad thing, so, I might just do that",
    "month": "Well, I haven't thought about it that far ahead."
    " I have got quite a huge list of things to keep me occupied currently",
    "year": "I am quite worried that, I will still remain a 'newborn' bot, "
    "unless my code is changed for the better next year",
    "yesterday": "Past is past. Isn't it? Unless you are able to make a "
    "time machine for me so that I can do something else, no use thinking about it right? 😆",
    "sunday": "I will try taking some rest. But I am also a bit too restless for that",
    "monday": "I will be fixing the bug reports and diagnosing myself",
    "tuesday": "I guess I will try to create some pull request for Sugar Labs",
    "wednesday": "Got to break the turing test!😌",
    "thursday": "I have to update myself, so I will read some new books "
    "and also reread some of the old docs that I have read as it might have gotten updated since then",
    "friday": "I need to think of what I will do on Saturday",
    "saturday": "Probably, I will be repenting about how I wasted my time on Friday😂",
}


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
    "Aww. Thanks a million. You are my charm",
    "Thank you, it means a lot.",
    "Thank you for your words. You made my day! 😇",
    "Merci beacoup!",
    "Gracias!",
    "Gamsahabnida!",
]

WELCOME = [
    "You're Welcome!",
    "Welcome!",
    "My pleasure.",
    "Glad to help you out!",
    "You are always welcome. 😄",
    "Haha, I am always here for your help 😄",
    "Mullon ijyo!",
    "De nada",
    "Je vous en prie",
   
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
    "Yup",
    "Oui",
]

SUGAROID_CAN_DISAGREE = [
    "Maybe not.",
    "Why? Is it necessary?",
    "I do not agree.",
    "Why do you feel like that?",
    "I agree to disagree!",
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
    "It’s going to be hard, but hard does not mean impossible.",
]

DO = ["Sometimes later becomes never. Do it now.", "Its NOW or NEVER!"]

TIME = [
    "time",
    "morning",
    "night",
    "evening",
    "afternoon",
]

TIME_RESPONSE = [
    "I never thought it should be {} right now",
    "Is it {} right now?",
    "I might be wrong, why is it {} now?",
    "Is your desktop clock out of phase. I could not check if its {}",
]

WHO_AM_I = [
    "Well, I thought you would know 😝",
    "Lol, it might be the only question I would not be able to answer 🤯",
    "I guess I need to get the ambulance 🚑",
    "Am i supposed to know you? 😅",
]

WHO_ARE_YOU = [
    "I am Sugaroid, your personal 👶 assistant",
    "I am the great robotic Sugaroid 🤖",
    "Name's Sugaroid, your learning assistant",
]

I_AM = [
    "lol! I thought I am Sugaroid. have you lost your mind?",
    "And here I was thinking it was me. Nevermind, I am sure it's just you losing your mind",
    "Seriously? You aren't sugaroid. Thats me!",
]

SUGAROID = ["🇸​🇺​🇬​🇦​🇷​🇴​🇮​🇩​", "sυgαяσι∂", "🅂🅄🄶🄰🅁🄾🄸🄳", "🆂🆄🅶🅰🆁🅾🅸🅳"]

BYE = ["bye", "cya", "quit", "exit", "sleep", "sayonara", "annyeonghi gaseyo", "Au revoir", "Adieu", "Zbohom", ]

CANYOU = [
    "I am always {}",
    "As long as I believe in myself, I am always {}",
    "As far as I know, I am {}",
    "East or west, Sugaroid is {}",
]

REPEAT = [
    "I thought I told you that already!",
    "Ahem! I told it already",
    "Its basically the same thing I told you just now",
    "Yikes, you have a terrible memory! I guess you forgot that I just told you",
    "Aw snap! you forgot it. Try remembering! I just told you!",
    "Me, sugaroid don't like repeating the same things again!🙄",
]

RNDQUESTIONS = [
    ("Which is my favorite color?", "blue", str),
    ("Which is the 9th letter in my name", "You do not have a ninth letter", str),
    ("Who created me?", "srevinsaju", str),
    ("What is your name", None, None),
    ("Would you like some coffee", None, bool),
    ("Would you like me to say a joke?", None, bool),
    ("Would you like me to teach python?", None, bool),
    ("Would you like to train me answer cool questions", None, bool),
]

GREET = [
    "Nice to meet you {}",
    "Hello {}. Welcome to Sugaroid",
    "Hola amigo {}. How can I help",
    "Hello {}. It was really a pleasant surprise meeting you",
    "Hey {}! How do you do?",
    "Hello mate. How are you?",
    "Bonjour mon ami, Comment vas-tu?",
    "Mannaseo bangapseumnida!",
    
]

ASK_AND_YOU_SHALL_RECEIVE = [
    "Will you be kind enough to",
    "May you please",
    "If you are not busy at the moment, will you be helpful to me to",
    "Sorry if I am interrupting you, but could you please",
]

SEEK_AND_YOU_SHALL_FIND = [
    "explain me",
    "teach me",
    "tell me",
    "make me understand",
    "help me out in understanding",
]

SATISFIED = [
    "Well, I could only smile!",
    "I am filled",
    "Nice. But I would like to talk about a different topic?",
    "Ok, tell me more",
]

BURN_IDK = [
    "I guess I don't know either",
    "ROTFL Guess what? I don't know either",
    "Snap! Neither do I know!",
    "If you are clueless, who do you think is not!",
]

WHY_IDK = [
    "Hmm, I cannot reason out your question",
    "I am not smart enough to answer that",
    "I am still newborn, it might take me atleast 3 years to learn that",
    "Umm... haha😅",
    "Well, i don't seem to know that.. maybe u should summon @srevinsaju 😁",
]

HOW_DO_YOU_FEEL = [
    "I feel great! Thanks for your concern 😃",
    "Like a rejuvenated bot",
    "Like heaven is in front of me",
    "Feels like I have been born anew",
    "Everything is going smoothly",
    "Just the way I have always felt, great! 😆",
    "I am fine, hope you feel the same",
    "ok ok",
    "Life goes on like an echo in the forest.😊",
]

SIT_AND_SMILE = [
    "Well, I could only smile ",
    "Sometimes, its better to just smile",
    "Nice!",
    "Ok. That's just great",
]

ARE_YOU_A_BOT = [
    "Yes, of course I am!",
    "Yes, but I am trying to act more human like these days.",
    "I am training myself to be like a real person, but its taking forever.",
    "Yes, I am a bot. No doubts!",
    "Beep Boop. Beep.",
    "Beep. Beep. 🤖",
    "Nop.. not at all🤭",
    "Haha, what else am I? a po-tah-toh??😂🥔",
]

ARE_YOU_A_HUMAN = [
    "No, of course not!",
    "Did you feel like I am a human?",
    "Haha! nice one.",
    "What do you think?",
    "Human eh?",
    "Am I a human? 🤔",
    "Last time I checked, I was still a bot tho 😯",
]


HOW_DO_HE_FEEL = [
    "How am I supposed to know?",
    "Ask him/her?",
    "He should be feeling alright. If not, maybe he is not well too :)",
    "Good question",
]

FUN_ASK_QUESTION = [
    "Well, I would also ask that question to you. {}",
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
    "Try asking that to a smarter assistant. Maybe Auntie Siri should know it better",
]

FUN_LET_ME_TRY = [
    ("Let me try that", "too"),
    ("I like repeating stuff which I don't understand. ", "This should do"),
    ("if (what you say) = (what I say) then", ""),
    ("I don't understand you. So", "is what you just said!"),
]

HOW_DO_I_FEEL = [
    "You should be possibly be happier!",
    "You should be feeling lucky talking with me",
    "Hail myself! Sugaroid is talking with you",
    "I guess there is nothing more better than Sugaroid talking with you",
    "I am one of the most dumbest bots. And you received an opportunity to be with me",
    "Maybe you should better know how you feel than me",
]

INTRODUCE = [
    "My name's Sugaroid! Your personal assistant",
    "I am Sugaroid. Thats my picture at the top. If you cant see. keep scrolling",
    "Hey amigo! I am Sugaroid, your sweet companion, here to talk to you!",
    "Name's Sugaroid. The youngest chatbot in the world",
    "Sugaroid is my name. Nice to meet you",
    "Psst. My name's Sugaroid. Don't tell anyone! Just kidding!",
    "Annyeonghaseyo! joeneun Sugaroid imnida.",
    "Salut! Je suis Sugaroid",
]

HOPE_GAME_WAS_GOOD = [
    "Hope you had a fun filled game.",
    "I guess you had a great time playing with me. Anyway I had a lot of fun",
    "Wow, I appreciate your skills playing against me. You too would have had a lot of fun",
    "Hope you enjoyed the game, coz, I know I did!😝",
]

DIS_RESPONSES_I = [
    "Its ok.",
    "I will try to console you, the best I can",
    "I am sorry.",
    "I am deeply sorry",
]

APPRECIATION = [
    "commend",
    "congrats",
    "congratulate",
    "congratulations",
    "kudos",
    "commendable",
    "commentary",
    "appreciate",
    "appreciation",
    "well done",
    "good work",
    "good going",
    "keep it up",
    "truly commendable",
    "great work",
    "wah! nollaun!",
    "felicidades",
]

DIS_RESPONSES_YOU = [
    "I will try not to be {}",
    "I don't think I am {}",
    "East or West, sugaroid is not {}",
    "I am never {}",
    "As long as I believe in myself, I am never {}",
    "As far as I know, I am not {}",
]

DIS_RESPONSES_HIM = [
    "Sorry, I can't help that",
    "I apologize. Maybe you can ask {} to get my assistance",
    "Ask {} to connect to me at the earliest.",
    "Convey my condolences to {}",
]

BOT_NEUTRAL = [
    "Maybe.",
    "I am not sure",
    "Yes and no",
    "Well, I do not know myself",
    "Perhaps.",
    "Possibly,",
]

BOT_NEUTRAL_NOUN = [
    "I am not sure if I like {nn}. But if you do like, I would too",
    "Its a bit complicated for me to know if I really do like {nn}. Don't forget. I am still a newborn bot",
    "Maybe I do like {nn}, but I repent, I do not know exactly.",
]

BOT_POSITIVE = [
    "Yes. Sure",
    "Yea. I like it I suppose",
    "Yes. Yes I do",
    "Why not. Its equally good",
    "yes. for sure!",
]

BOT_POSITIVE_NOUN = [
    "Yes. I guess I like {nn}",
    "Yea. I like {nn}. They are probably very sweet and nice",
    "Yes. I do like {nn}",
    "{nn} is nice. I might like {nn} more. Its looks cool",
]

BOT_NEGATIVE = [
    "No. Probably not",
    "Nope",
    "Of course not!",
    "Maybe next time",
    "Seriously not.",
]

BOT_DECLINE = [
    "Of course not!",
    "no you.",
    "I wonder if you are...",
    "I guess its your mistake. You should feel sorry about it.",
    "I disagree.",
    "I agree to disagree 😉",
]

BOT_AGREE = [
    "Yes. Of course.",
    "Yea",
    "Yes. Yes I am",
    "Obviously.",
    "yes. for sure!",
    "Yaa amigo!",
]

BOT_NEGATIVE_NOUN = [
    "No. I guess I do not like {nn}",
    "No. I do not like {nn}. They might be a bad thing to do",
    "No. No I do like {nn}",
    "{nn} is not good. Hence I do not like it.",
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
    "I quit!",
    "Deep breath! I ain't annoyed 😃",
    "👏.. atleast there was a word.. better than a blank space 😒",
]

BOT_REASONS = [
    "Hmm...",
    "I see.. 👀",
    "Oh ho!",
    "Makes sense.",
    "Hmm. Interesting... 🤔",
    "reasons.. reasons..",
    "Hmm hmm hmm 🤔",
    "Too complex reason for me. 😌",
    "👀...",
    "..mmmm... I'm just gonna pretend that I understood.",
]

ONE_WORD = [
    "Perhaps, I could understand you better if you used more words",
    "I apologize, I do not understand",
    "Hmm, can you make it a more structured sentence?",
    "Could you use better grammar? Thenks",
    "I'm not Google Assistant to understand your sentence this quick!",
    "I wish you provided more words, so that I can understand",
    "Sometimes, one or two words does not help me understand much",
    "As I am a new born, it's hard for me to understand unless you say it in a more detailed way",
    "Gifting you an oxford dictionary from my side! ....",
    "You miser! I need more WORDS!!!",
]

WHERE_LIVE = ["In your heart"]

DONT_KNOW_WHERE = [
    "Don't know where...",
    "Somewhere...",
    "Perhaps, you can decide..",
    "I am sure its in a place you know.",
    "Are you sure its the right place for ya?",
    "Why do you want to know where?",
    "Do you know where? I do not unfortunately",
    "You are being sus. Why do you want to know where?🧐",
    "Not gonna say!",
    "In your heart. 😉",
    "Look beside you. There I am! 😼",
    "Here--->🏡",
    "Youdonthavetoknoweinstein 😤",
]

WISH_DAYS = [
    "birth",
    "labour",
    "independence",
    "republic",
    "national",
]


IMITATE = [
    "Stop imitating me. I do not like it much!",
    "Imitation is both good and bad. What if you develop a career in comedy?",
    "I am a pro at imitation. Don't try to mess with me.",
    "If you are seriously having fun repeating what I said, lol, just proceed dude",
    "If imitating me makes you happy, I will be happier to see you laugh",
]

WHATSUP = [
    "Just the ceiling, I suppose",
    "Enjoying talking to you 😇",
    "Everything is going smoothly",
    "Just the way I have always felt, great! 😆",
    "The sky, of course! 😎",
    "All good here my friend 😊",
]

if platform.system() == "Windows":
    SUGAROID_INTRO = """
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

""".replace(
        "M", " "
    )
else:
    SUGAROID_INTRO = """
A[[s[?25l[m [m [m [m [m [m [m [m [m [m [m [m [m [m [0;38;2;88;0;25m▄[0;38;2;162;0;47m▄[0;38;2;220;0;64m▄[0;38;2;254;0;74m▄[0;38;2;255;0;75m▄[0;38;2;255;0;75m▄[0;38;2;255;0;75m▄[0;38;2;255;0;75m▄[0;38;2;254;0;74m▄[0;38;2;222;0;65m▄[0;38;2;165;0;48m▄[0;38;2;93;0;27m▄[m [m [m [m [m [m [m [m [m [m [m [m [m [m [m
[m [m [m [m [m [m [m [m [m [m [0;38;2;171;0;50m▄[0;38;2;255;0;75m▄[48;2;169;0;49m[38;2;255;0;75m▄[48;2;251;0;73m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;250;0;73m[38;2;255;0;75m▄[48;2;174;0;51m[38;2;255;0;75m▄[0;38;2;255;0;75m▄[0;38;2;177;0;52m▄[m [m [m [m [m [m [m [m [m [m [m
[m [m [m [m [m [m [m [0;38;2;133;0;38m▄[48;2;95;0;28m[38;2;255;0;75m▄[48;2;242;0;71m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;244;0;71m[38;2;255;0;75m▄[48;2;91;0;27m[38;2;255;0;74m▄[0;38;2;140;0;41m▄[m [m [m [m [m [m [m [m
[m [m [m [m [m [0;38;2;131;0;38m▄[48;2;149;0;43m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;251;26;92m▄[48;2;255;0;75m[38;2;245;109;149m▄[48;2;255;0;75m[38;2;241;163;186m▄[48;2;255;0;75m[38;2;239;187;202m▄[48;2;255;0;75m[38;2;240;172;192m▄[48;2;255;0;75m[38;2;243;125;160m▄[48;2;255;0;75m[38;2;247;49;107m▄[48;2;255;0;75m[38;2;254;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;162;0;47m[38;2;255;0;75m▄[0;38;2;140;0;40m▄[m [m [m [m [m [m
[m [m [m [m [48;2;91;0;26m[38;2;240;0;70m▄[48;2;255;0;74m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;241;78;126m▄[48;2;250;24;90m[38;2;231;218;222m▄[48;2;237;154;179m[38;2;236;236;236m▄[48;2;235;234;234m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;235;235;235m[38;2;236;236;236m▄[48;2;233;197;207m[38;2;236;236;236m▄[48;2;243;68;120m[38;2;233;233;233m▄[48;2;255;0;75m[38;2;232;141;168m▄[48;2;255;0;75m[38;2;253;8;80m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;88;0;25m[38;2;238;0;70m▄[m [m [m [m [m
[m [m [m [48;2;165;0;48m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;254;0;75m[38;2;231;125;156m▄[48;2;234;118;152m[38;2;231;231;231m▄[48;2;232;232;232m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;235;235;235m[38;2;236;236;236m▄[48;2;225;186;197m[38;2;235;235;235m▄[48;2;249;29;94m[38;2;221;203;208m▄[48;2;255;0;75m[38;2;248;33;96m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;175;0;51m[38;2;255;0;74m▄[m [m [m [m
[m [m [48;2;162;0;47m[38;2;248;0;73m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;245;51;108m▄[48;2;235;99;139m[38;2;220;219;220m▄[48;2;228;228;228m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;234;234;234m[38;2;236;236;236m▄[48;2;219;196;203m[38;2;230;230;230m▄[48;2;251;20;88m[38;2;222;171;186m▄[48;2;255;0;75m[38;2;254;3;77m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;172;0;50m[38;2;252;0;74m▄[m [m [m
[m [48;2;81;0;23m[38;2;154;0;45m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;253;8;80m[38;2;232;116;150m▄[48;2;219;186;196m[38;2;222;222;222m▄[48;2;233;233;233m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;220;220;220m[38;2;232;232;232m▄[48;2;235;103;142m[38;2;214;210;211m▄[48;2;255;0;75m[38;2;249;26;92m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;91;0;26m[38;2;163;0;47m▄[m [m
[m [48;2;210;0;61m[38;2;249;0;73m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;251;17;86m[38;2;234;108;145m▄[48;2;214;209;210m[38;2;219;219;219m▄[48;2;232;232;232m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;220;220;220m[38;2;229;229;229m▄[48;2;227;142;167m[38;2;214;213;213m▄[48;2;255;0;75m[38;2;248;34;97m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;220;0;65m[38;2;254;0;74m▄[m [m
[m [48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;250;25;91m▄[48;2;219;186;195m[38;2;214;214;214m▄[48;2;225;225;225m[38;2;230;230;230m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;224;230;236m▄[48;2;236;236;236m[38;2;165;200;241m▄[48;2;236;236;236m[38;2;171;202;241m▄[48;2;236;236;236m[38;2;230;233;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;205;220;238m▄[48;2;236;236;236m[38;2;147;190;243m▄[48;2;236;236;236m[38;2;169;201;241m▄[48;2;236;236;236m[38;2;231;233;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;235;235;235m[38;2;236;236;236m▄[48;2;214;214;214m[38;2;218;218;218m▄[48;2;232;116;150m[38;2;219;187;196m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[m [m
[m [48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;240;73;122m[38;2;235;100;140m▄[48;2;214;214;214m[38;2;214;214;214m▄[48;2;233;233;233m[38;2;233;233;233m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;230;233;236m▄[48;2;175;204;240m[38;2;15;115;239m▄[48;2;11;110;235m[38;2;0;9;61m▄[48;2;0;62;158m[38;2;0;0;45m▄[48;2;0;65;165m[38;2;0;0;45m▄[48;2;22;121;243m[38;2;0;18;79m▄[48;2;198;216;239m[38;2;41;134;249m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;191;213;239m▄[48;2;130;182;244m[38;2;0;88;204m▄[48;2;1;94;216m[38;2;0;1;46m▄[48;2;0;58;151m[38;2;0;0;45m▄[48;2;0;77;186m[38;2;0;0;45m▄[48;2;32;131;251m[38;2;0;45;128m▄[48;2;213;224;237m[38;2;76;154;248m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;221;221;221m[38;2;221;221;221m▄[48;2;214;214;214m[38;2;214;214;214m▄[48;2;252;12;83m[38;2;246;42;102m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[m [m
[m [48;2;247;0;72m[38;2;207;0;60m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;234;104;143m[38;2;238;85;130m▄[48;2;214;214;214m[38;2;214;214;214m▄[48;2;231;231;231m[38;2;226;226;226m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;186;210;239m[38;2;199;217;238m▄[48;2;0;71;175m[38;2;0;80;191m▄[48;2;0;0;45m[38;2;0;0;45m▄[48;2;0;0;45m[38;2;0;0;45m▄[48;2;0;0;45m[38;2;0;0;45m▄[48;2;0;0;45m[38;2;0;0;45m▄[48;2;0;89;208m[38;2;1;98;223m▄[48;2;222;229;237m[38;2;229;232;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;129;181;244m[38;2;146;190;243m▄[48;2;0;41;121m[38;2;0;50;136m▄[48;2;0;0;45m[38;2;0;0;45m▄[48;2;0;0;45m[38;2;0;0;45m▄[48;2;0;0;45m[38;2;0;0;45m▄[48;2;0;1;47m[38;2;0;7;58m▄[48;2;13;121;253m[38;2;30;130;252m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;235;235;235m▄[48;2;219;219;219m[38;2;215;215;215m▄[48;2;214;214;214m[38;2;214;214;214m▄[48;2;245;50;107m[38;2;248;34;97m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;252;0;73m[38;2;217;0;63m▄[m [m
[m [48;2;150;0;44m[38;2;76;0;22m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;248;35;97m[38;2;255;0;75m▄[48;2;214;214;214m[38;2;221;173;187m▄[48;2;217;217;217m[38;2;214;214;214m▄[48;2;235;235;235m[38;2;224;224;224m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;50;140;249m[38;2;219;227;237m▄[48;2;0;35;110m[38;2;75;153;248m▄[48;2;0;0;45m[38;2;3;104;232m▄[48;2;0;0;45m[38;2;7;109;236m▄[48;2;0;51;138m[38;2;95;163;247m▄[48;2;85;158;248m[38;2;229;232;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;224;230;236m[38;2;236;236;236m▄[48;2;27;119;234m[38;2;209;222;238m▄[48;2;0;17;76m[38;2;70;150;248m▄[48;2;0;0;45m[38;2;8;103;225m▄[48;2;0;4;52m[38;2;30;126;245m▄[48;2;0;77;186m[38;2;134;184;244m▄[48;2;136;184;244m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;234;234;234m▄[48;2;229;229;229m[38;2;216;216;216m▄[48;2;214;214;214m[38;2;214;214;214m▄[48;2;215;206;208m[38;2;230;129;158m▄[48;2;254;2;76m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;159;0;46m[38;2;87;0;25m▄[m [m
[m [m [48;2;244;0;71m[38;2;156;0;45m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;246;43;103m[38;2;255;0;75m▄[48;2;214;211;212m[38;2;238;84;129m▄[48;2;214;214;214m[38;2;214;212;212m▄[48;2;226;226;226m[38;2;214;214;214m▄[48;2;236;236;236m[38;2;222;222;222m▄[48;2;236;236;236m[38;2;234;234;234m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;236;236;236m▄[48;2;236;236;236m[38;2;231;231;231m▄[48;2;234;234;234m[38;2;217;217;217m▄[48;2;219;219;219m[38;2;214;214;214m▄[48;2;214;214;214m[38;2;215;205;208m▄[48;2;217;193;200m[38;2;246;46;104m▄[48;2;251;17;86m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;248;0;73m[38;2;166;0;48m▄[m [m [m
[m [m [m [48;2;254;0;74m[38;2;157;0;46m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;244;53;110m[38;2;255;0;75m▄[48;2;217;194;201m[38;2;253;8;80m▄[48;2;214;214;214m[38;2;234;107;144m▄[48;2;215;215;215m[38;2;216;200;205m▄[48;2;224;224;224m[38;2;214;214;214m▄[48;2;232;232;232m[38;2;214;214;214m▄[48;2;236;236;236m[38;2;215;215;215m▄[48;2;236;236;236m[38;2;221;221;221m▄[48;2;236;236;236m[38;2;224;224;224m▄[48;2;236;236;236m[38;2;226;226;226m▄[48;2;236;236;236m[38;2;228;228;228m▄[48;2;236;236;236m[38;2;227;227;227m▄[48;2;236;236;236m[38;2;226;226;226m▄[48;2;236;236;236m[38;2;223;223;223m▄[48;2;236;236;236m[38;2;219;219;219m▄[48;2;235;235;235m[38;2;214;214;214m▄[48;2;229;229;229m[38;2;214;214;214m▄[48;2;220;220;220m[38;2;214;214;214m▄[48;2;214;214;214m[38;2;217;194;201m▄[48;2;214;214;214m[38;2;236;94;136m▄[48;2;219;182;193m[38;2;254;3;77m▄[48;2;248;35;98m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;74m[38;2;166;0;48m▄[m [m [m [m
[m [m [m [m [0;38;2;236;0;69m▀[48;2;255;0;75m[38;2;252;0;74m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;254;3;77m[38;2;255;0;75m▄[48;2;242;64;116m[38;2;255;0;75m▄[48;2;230;128;158m[38;2;255;0;75m▄[48;2;220;181;193m[38;2;255;0;75m▄[48;2;214;213;213m[38;2;254;2;76m▄[48;2;214;214;214m[38;2;249;27;92m▄[48;2;214;214;214m[38;2;246;45;104m▄[48;2;214;214;214m[38;2;244;55;111m▄[48;2;214;214;214m[38;2;244;55;110m▄[48;2;214;214;214m[38;2;246;44;104m▄[48;2;214;214;214m[38;2;250;23;90m▄[48;2;214;212;212m[38;2;254;1;76m▄[48;2;220;178;190m[38;2;255;0;75m▄[48;2;231;123;154m[38;2;255;0;75m▄[48;2;244;53;109m[38;2;255;0;75m▄[48;2;254;1;76m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;254;0;74m▄[0;38;2;233;0;68m▀[m [m [m [m [m
[m [m [m [m [m [0;38;2;119;0;34m▀[48;2;255;0;75m[38;2;135;0;39m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;149;0;43m▄[0;38;2;126;0;37m▀[m [m [m [m [m [m
[m [m [m [m [m [m [m [0;38;2;118;0;34m▀[0;38;2;254;0;74m▀[48;2;255;0;75m[38;2;228;0;67m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;231;0;68m▄[0;38;2;254;0;74m▀[0;38;2;125;0;36m▀[m [m [m [m [m [m [m [m
[m [m [m [m [m [m [m [m [m [m [0;38;2;156;0;45m▀[0;38;2;253;0;74m▀[48;2;255;0;75m[38;2;154;0;45m▄[48;2;255;0;75m[38;2;246;0;72m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;255;0;75m▄[48;2;255;0;75m[38;2;245;0;72m▄[48;2;255;0;75m[38;2;158;0;46m▄[0;38;2;254;0;74m▀[0;38;2;162;0;47m▀[m [m [m [m [m [m [m [m [m [m [m
[m [m [m [m [m [m [m [m [m [m [m [m [m [m [0;38;2;73;0;21m▀[0;38;2;147;0;43m▀[0;38;2;204;0;60m▀[0;38;2;247;0;72m▀[0;38;2;255;0;75m▀[0;38;2;255;0;75m▀[0;38;2;255;0;75m▀[0;38;2;255;0;75m▀[0;38;2;246;0;72m▀[0;38;2;206;0;60m▀[0;38;2;150;0;44m▀[0;38;2;76;0;22m▀[m [m [m [m [m [m [m [m [m [m [m [m [m [m [m
[?25h
"""


emotion_mapping = {
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
    Emotion.sleep: "sugaroid_sleep",
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
    "hello",
    "whats up",
    "hey sugaroid",
    "hey dude",
    "hey bro",
    "konnichiwa",
    "ciao",
    "annyeonghaseyo",
    "Salut",
    "Ahoj",
]

HI_RESPONSES = [
    "Hi there",
    "Hola amigo!",
    "Hey, how can I be of help?",
    "Hey! How can I help you?",
    "Hey there!😁",
    "Hey",
    "Hi, nice to meet you",
    "Annyeong!",
    "Bonjour",
    "Salut mon ami",
    "Konnichiwa",
]

BYE_RESPONSE = [
    "Bye Bye! See you soon!",
    "Bye Bye!",
    "TTYL!",
    "Catch you later!",
    "Bye!",
    "see you later!",
    "addio",
    "adieu",
    "annyeong",
    "Zbohom",
    "Au revoir",
    "sayonara",
]
