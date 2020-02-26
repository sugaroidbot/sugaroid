from django.db import models


class Chatbot(models.Model):
    user = models.TextField()
