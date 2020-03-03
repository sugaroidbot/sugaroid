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
