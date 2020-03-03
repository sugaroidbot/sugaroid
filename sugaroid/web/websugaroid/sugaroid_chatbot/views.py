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
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from sugaroid.sugaroid import Sugaroid


sg = Sugaroid()


class Conversation:
    def __init__(self, by=None, message=None):
        self.by = by
        self.message = message


def reinit_cookie(request):
    response = HttpResponseRedirect('/')
    response.set_cookie('conversation', '[]')
    return response


def index(request):
    print("H"*5, request.COOKIES.get('conversation'))
    if request.COOKIES.get('conversation') is None:
        return reinit_cookie(request)
    else:
        if eval(request.COOKIES.get('conversation')) is None:
            return reinit_cookie(request)
        print("J"*55, request.COOKIES.get('conversation'))
        conversation_local = [[x[0], x[1]] for x in eval(request.COOKIES.get('conversation'))]
        response = render(request, 'app.html', {'all_items': [Conversation(x[0], x[1]) for x in conversation_local]})
        response.set_cookie('conversation', '{}'.format(conversation_local))

        return response


def post_user_input(request):
    print("K"*6, request.COOKIES.get('conversation'))
    c = request.POST['userInput']

    if c and c.isspace():
        return HttpResponseRedirect('/')

    conversation_local = eval(request.COOKIES.get('conversation'))
    conversation_local.append(['replies', c])
    # import pdb; pdb.set_trace()
    response = HttpResponseRedirect('/chatbot')
    print("SETTING COOKIE", conversation_local)

    response.set_cookie('conversation', str(conversation_local))
    return response


def get_chatbot_response(request):
    print("D"*5, "K"*6, request.COOKIES.get('conversation'))
    conversation_local = eval(request.COOKIES.get('conversation'))
    r = str(sg.parse(conversation_local[-1][1]))
    conversation_local.append(['sent', r])
    response = HttpResponseRedirect('/')
    response.set_cookie('conversation', '{}'.format(conversation_local))
    return response
