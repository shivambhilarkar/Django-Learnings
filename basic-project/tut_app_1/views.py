from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question
# Create your views here.

def welcome_page(request):
    return HttpResponse("<h1> Welcome to our website...!</h1>")


def home_page(request):
    # load the html template
    home_page_template = loader.get_template("tut_app_1/index.html")
    return HttpResponse(home_page_template.render(context={} , request= request))

def questions_page(request):
    question_page_template = loader.get_template("tut_app_1/questions.html")
    all_questions = Question.objects.all()
    return HttpResponse(question_page_template.render(context={ 'questions' : all_questions}, request= request))