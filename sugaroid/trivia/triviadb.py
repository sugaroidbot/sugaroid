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
db = \
    {
        1: {
            "category": "History",
            "type": "boolean",
            "difficulty": "hard",
            "question": "Japan was part of the Allied Powers during World War I.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        2: {
            "category": "Animals",
            "type": "boolean",
            "difficulty": "medium",
            "question": "An octopus can fit through any hole larger than its beak.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        3: {
            "category": "Celebrities",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Michael Jackson had a pet python named &lsquo;Crusher&rsquo;.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        4: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Matt Damon played an astronaut stranded on an extraterrestrial planet in both of the movies Interstellar and The Martian.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        5: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Super Mario Bros. was released in 1990.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        6: {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Linus Torvalds created Linux and Git.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        7: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The 2010 film ';The Social Network'; is a biographical drama film about MySpace founder Tom Anderson.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        8: {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        9: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The word ';Inception'; came from the 2010 blockbuster hit ';Inception';.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        10: {
            "category": "Entertainment: Books",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The book 1984 was published in 1949.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        11: {
            "category": "Entertainment: Music",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Ashley Frangipane performs under the stage name Halsey.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        12: {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "medium",
            "question": "An eggplant is a vegetable.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        13: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Metal Gear Solid V: The Phantom Pain runs on the Fox Engine.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        14: {
            "category": "Mythology",
            "type": "boolean",
            "difficulty": "easy",
            "question": "According to Greek Mythology, Zeus can control lightning.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        15: {
            "category": "Geography",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Gothenburg is the capital of Sweden.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        16: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "easy",
            "question": "In ';Super Mario 3D World';, the Double Cherry power-up originated from a developer accidentally making two characters controllable.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        17: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Shaquille O&#039;Neal appeared in the 1997 film ';Space Jam';.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        18: {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "You can legally drink alcohol while driving in Mississippi.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        19: {
            "category": "Science: Mathematics",
            "type": "boolean",
            "difficulty": "hard",
            "question": "If you could fold a piece of paper in half 50 times, its&#039; thickness will be 3/4th the distance from the Earth to the Sun.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        20: {
            "category": "Mythology",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The Japanese god Izanagi successfully returned his wife Izanami from the Underworld.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        21: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The PlayStation was originally a joint project between Sega and Sony that was a Sega Genesis with a disc drive.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        22: {
            "category": "Animals",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Rabbits are rodents.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        23: {
            "category": "Geography",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The capital of the US State Ohio is the city of Chillicothe.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        24: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "easy",
            "question": "In the original Star Wars trilogy, David Prowse was the actor who physically portrayed Darth Vader.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        25: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "hard",
            "question": "';Cube';, ';Cube 2: Hypercube'; and ';Cube Zero'; were directed by the same person.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        26: {
            "category": "Science: Computers",
            "type": "boolean",
            "difficulty": "hard",
            "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        27: {
            "category": "Entertainment: Music",
            "type": "boolean",
            "difficulty": "easy",
            "question": "A Saxophone is a brass instrument.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        28: {
            "category": "Entertainment: Television",
            "type": "boolean",
            "difficulty": "easy",
            "question": "In Battlestar Galactica (2004), Cylons were created by man as cybernetic workers and soldiers.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        29: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "easy",
            "question": "';Minions'; was released on the June 10th, 2015.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        30: {
            "category": "History",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Adolf Hitler was tried at the Nuremberg trials.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        31: {
            "category": "Entertainment: Music",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Pink Guy&#039;s debut album was ';Pink Season';.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        32: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "hard",
            "question": "All of these maps were in ';Tom Clancy&#039;s Rainbow Six Siege'; on its initial release: House, Clubhouse, Border, Consulate.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        33: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "medium",
            "question": "In the video game ';Transistor';, ';Red'; is the name of the main character.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        34: {
            "category": "Entertainment: Television",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Bob Ross was a US Air Force pilot.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        35: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Resident Evil 4 was originally meant to be a Nintendo GameCube exclusive.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        36: {
            "category": "Entertainment: Television",
            "type": "boolean",
            "difficulty": "easy",
            "question": "In ';Doctor Who';, the Doctor gets his TARDIS by stealing it.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        37: {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "medium",
            "question": "';Santa Claus'; is a variety of melon.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        38: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "medium",
            "question": "In ';Call Of Duty: Zombies';, you can upgrade the ';Apothicon Servant'; in the ';Shadows Of Evil'; map.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        39: {
            "category": "Entertainment: Music",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Nick Mason is the only member to appear on every Pink Floyd album.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        40: {
            "category": "Entertainment: Video Games",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The game ';Pocket Morty'; has a Morty called ';Pocket Mortys Morty';?",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        41: {
            "category": "Entertainment: Music",
            "type": "boolean",
            "difficulty": "easy",
            "question": "In 1993, Prince changed his name to an unpronounceable symbol because he was unhappy with his contract with Warner Bros.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        42: {
            "category": "Entertainment: Music",
            "type": "boolean",
            "difficulty": "easy",
            "question": "The 2011 movie ';The Adventures of Tintin'; was directed by Steven Spielberg.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        43: {
            "category": "Geography",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Rhode Island is actually located on the US mainland, despite its name.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        44: {
            "category": "Science & Nature",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Not including false teeth; A human has two sets of teeth in their lifetime.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        45: {
            "category": "Entertainment: Cartoon & Animations",
            "type": "boolean",
            "difficulty": "medium",
            "question": "Blue Danube was one of the musical pieces featured in Disney&#039;s 1940&#039;s film Fantasia.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        46: {
            "category": "Entertainment: Music",
            "type": "boolean",
            "difficulty": "medium",
            "question": "A Facebook campaign placed Rage Against The Machine&#039;s ';Killing in the Name Of'; as the UK Christmas Number 1 in 2009.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        47: {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "A pasodoble is a type of Italian pasta sauce.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        48: {
            "category": "Entertainment: Japanese Anime & Manga",
            "type": "boolean",
            "difficulty": "hard",
            "question": "The character Plum from ';No Game No Life'; is a girl.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        49: {
            "category": "General Knowledge",
            "type": "boolean",
            "difficulty": "easy",
            "question": "Slovakia is a member of European Union-",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        50: {
            "category": "Entertainment: Film",
            "type": "boolean",
            "difficulty": "medium",
            "question": "The original ending of ';Little Shop Of Horrors'; has the plants taking over the world.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        }
    }
