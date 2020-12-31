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

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

News headlines provided by NewsAPI
"""
import logging
import os

from chatterbot.logic import LogicAdapter
from newsapi import NewsApiClient
from dotenv import load_dotenv
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import spac_token

from sugaroid.sugaroid import SugaroidStatement

NEWSAPI_COUNTRIES = {
    'argentina': 'ar', 'australia': 'au', 'austria': 'at', 'belgium': 'be', 'brazil': 'br',
    'bulgaria': 'bg', 'canada': 'ca', 'china': 'cn', 'colombia': 'co', 'cuba': 'cu',
    'czech republic': 'cz', 'egypt': 'eg', 'france': 'fr', 'germany': 'de', 'greece': 'gr',
    'hong kong': 'hk', 'hungary': 'hu', 'india': 'in', 'indonesia': 'id', 'ireland': 'ie',
    'israel': 'il', 'italy': 'it', 'japan': 'jp', 'latvia': 'lv', 'lithuania': 'lt',
    'malaysia': 'my', 'mexico': 'mx', 'morocco': 'ma', 'netherlands': 'nl', 'new zealand': 'nz',
    'nigeria': 'ng', 'norway': 'no', 'philippines': 'ph', 'poland': 'pl', 'portugal': 'pt',
    'romania': 'ro', 'russia': 'ru', 'saudi arabia': 'sa', 'serbia': 'rs', 'singapore': 'sg',
    'slovakia': 'sk', 'slovenia': 'si', 'south africa': 'za', 'south korea': 'kr', 'sweden': 'se',
    'switzerland': 'ch', 'taiwan': 'tw', 'thailand': 'th', 'turkey': 'tr', 'uae': 'ae',
    'ukraine': 'ua', 'united kingdom': 'gb', 'united states': 'us', 'venuzuela': 've',
    'us': 'us', 'uk': 'uk', 'u.k.': 'uk', 'u.s.': 'us', 'u.s': 'us', 'u.k': 'uk', 'u s': 'us', 'u k': 'uk',
    'the united states': 'us', 'the united kingdom': 'uk'
}


class SugaroidNews:
    """
    A dedicated class for processing news from the API
    """

    def __init__(self, chatbot=None):
        load_dotenv()
        self.chatbot = chatbot
        token = os.getenv('NEWSAPI_TOKEN')
        self.api = NewsApiClient(api_key=token)

    def get_top_headlines(self, country=None):
        """
        Get the top news items of the country if provided. Otherwise give international news
        :param country:
        :return:
        """
        try:
            if country is None:
                response = self.api.get_top_headlines()
            else:
                response = self.api.get_top_headlines(country=country)
            return self.process(response)
        except Exception as e:
            if str(e) == 'invalid country':
                self.chatbot.globals['last_news'] = False
                logging.info(
                    f'SugaroidNews: Failed to get the news. country=[{type(country)}, {country}]')
                return ['The country you provided does not exist in my database. I am sorry.']
            self.chatbot.globals['last_news'] = False
            return ['Failed to establish connection with the server. Error: {}'.format(e)]

    def get_news_keyword(self, keyword):
        try:
            response = self.api.get_everything(q=keyword)
            return self.process(response)
        except Exception as e:
            self.chatbot.globals['last_news'] = False
            return ['Failed to establish connection with the server. Error: {}'.format(e)]

    def process(self, response):
        """
        Convert the raw JSON Response to Human Readable News bullets
        :param response:
        :return: array of news headlines
        """

        news_headlines = []
        for i in response['articles']:
            try:
                news_headlines.append("{} from {}".format(
                    i['title'], i['source']['name']))
            except Exception as e:
                pass
        if not news_headlines:
            self.chatbot.globals['last_news'] = False
            return ['There was an error collecting the latest news headlines. Please try again later.']
        self.chatbot.globals['last_news'] = response
        return news_headlines


class NewsAdapter(LogicAdapter):
    """
    Ports the SugaroidNews Wrapper for easier access by the SugaroidChatbot Class
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.cos = None
        self.integer = False

    def can_process(self, statement):
        """
        Checks if the statement has a cosine similarity of any of the words mentioned here
        :param statement: SugaroidStatement Class Object
        :return: bool,
        """
        _ = self.chatbot.lp.similarity
        try:
            last_type = self.chatbot.globals['history']['types'][-1]
        except IndexError:
            last_type = False

        logging.info(
            'NewsAdapter: can_process() last_adapter was {}'.format(last_type))
        processed = str(statement).replace('?', '').replace('.', '')
        self.cos = max([
            _(processed, 'Whats happening'),
            _(processed, 'Get me the latest headlines'),
            _(processed, 'Show me today\'s news'),
            _(processed, 'Can you tell me todays news'),
            _(processed, 'Can you show me today\'s headlines'),
            _(processed, 'What is happening today'),
            _(processed, 'What top stories running right now')

        ])
        logging.info(
            "NewsAdapter received a cosine similarity of {}".format(self.cos))
        if self.cos > 0.8 or 'news' in processed.lower() or 'headlines' in processed.lower():
            return True
        elif 'show me more' in str(statement).lower() and self.chatbot.globals['last_news']:
            for i in spac_token(statement, self.chatbot):
                if i.tag_ in ['LS', 'CD']:
                    self.integer = i.lower_
                    return True
            else:
                return False
        elif self.chatbot.globals['last_news'] and (last_type == 'NewsAdapter'):
            for i in spac_token(statement, self.chatbot):
                if i.tag_ in ['LS', 'CD']:
                    self.integer = i.lower_
                    return True
            else:
                return False
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):

        confidence = self.cos
        country = None
        keyword = False
        # Override the other answer when asked for
        normalize = spac_token(statement, self.chatbot)
        if len(normalize) <= 2:
            confidence = confidence + 0.5
        if self.integer and self.chatbot.last_news:
            response = "Your selected integer {}, response {}".format(
                self.integer, self.chatbot.last_news)
            try:
                self.integer = int(self.integer)
            except ValueError:
                response = 'Sorry, I couldn\'t make out what number it actually is. I might understand it better if ' \
                           'it is in a numerical form? '
            if isinstance(self.integer, int):
                try:
                    data = self.chatbot.last_news['articles'][self.integer - 1]
                    provider = data['source']['name']
                    author = data['author']
                    last_updated = data['publishedAt']
                    title = data['title']
                    description = data['description']
                    url = data['url']
                    img_url = data['urlToImage']
                    response = f"From {provider}\nWritten by {author} on {last_updated}\n\n{title}\n\n{description}" \
                               f"\nRead more at {url}\n{img_url} "

                except IndexError:
                    response = "I am sorry. I couldn't find the item you actually asked for."
        else:
            for ent in normalize.ents:
                if ent.label_ == 'GPE':
                    country = ent
                elif ent.label_ in ['PERSON', 'NORP', 'FAC', 'ORG', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW']:
                    keyword = ent
            logging.info("NewsAdapter found as Natural Entity Recognizer words, country : {}, keyword: {}"
                         .format(country, keyword))
            for i in range(len(normalize) - 1):
                if normalize[i].lower_ == "about" or normalize[i].lower_ == 'on':
                    logging.info("NewsAdapter: found determiner about or on")
                    if not keyword:
                        keyword_words = []
                        for j in range(i + 1, len(normalize)):
                            if normalize[j].pos_ == 'DET':
                                continue
                            else:
                                keyword_words.append(normalize[j].text)

                        keyword = ' '.join(keyword_words)
            sg_news = SugaroidNews(self.chatbot)
            if keyword:
                logging.info(
                    "NewsAdapter: Getting news of keyword {}".format(keyword))
                news = sg_news.get_news_keyword(str(keyword))
            else:
                logging.info(
                    "NewsAdapter: Getting news of country {}".format(country))
                news = sg_news.get_top_headlines(
                    country=NEWSAPI_COUNTRIES.get(str(country).lower(), None))

            def bracketize(x):
                return '\n:large_blue_diamond: [{}] {}'.format(x[0] + 1, str(x[1]))

            response = ' '.join([bracketize(x) for x in enumerate(news)])

        selected_statement = SugaroidStatement(response, chatbot=True)
        selected_statement.confidence = confidence
        emotion = Emotion.neutral
        selected_statement.adapter = 'NewsAdapter'
        selected_statement.emotion = emotion

        return selected_statement
