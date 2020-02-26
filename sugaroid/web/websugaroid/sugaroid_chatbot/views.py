from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from sugaroid.sugaroid import Sugaroid

conversation = list()
sg = Sugaroid()

class Conversation:
    def __init__(self, by=None, message=None):
        self.by = by
        self.message = message


def index(request):
    return render(request, 'app.html',
                  {
                      'all_items': conversation
                  })


def post_user_input(request):
    c = request.POST['userInput']
    if c and c.isspace():
        return HttpResponseRedirect('/')
    conversation.append(Conversation('replies', "{}".format(c)))
    return HttpResponseRedirect('/chatbot')


def get_chatbot_response(request):
    response = str(sg.parse(conversation[-1].message))
    conversation.append(Conversation('sent', "{}".format(response)))
    return HttpResponseRedirect('/')
