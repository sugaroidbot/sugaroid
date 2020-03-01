import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup


def chatbot_query(query, index=0, total=2):
    fallback = 'Sorry, I cannot think of a reply for that. Error Code : {}'
    result = ''

    try:
        search_result_list = list(
            search(query, tld="com", num=total, stop=10, pause=0.5))

        page = requests.get(search_result_list[index])

        tree = html.fromstring(page.content)

        soup = BeautifulSoup(page.content, features="lxml")

        article_text = ''
        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text=True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            {ord(c): None for c in string.whitespace}
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback.format("SOME RANDOM ERROR")
        result = result.lstrip('Advertisement').lstrip('Supported by')
        return result
    except Exception as e:
        if len(result) == 0:
            result = fallback.format(e)
        return result
