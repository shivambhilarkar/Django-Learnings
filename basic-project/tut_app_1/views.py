from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
import logging

logger = logging.getLogger('todo_crud_app')

from .models import Question, Todo
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

def todo_page(request):
    if request.method == 'POST':
        form_input = request.POST
        logger.info(f'form input : {form_input}')
        if str(form_input['todo_input_text']).strip() != '':
            new_todo = Todo(task_text = form_input['todo_input_text'], created_date = timezone.now())
            new_todo.save()
        return HttpResponseRedirect('/todo/') # this will fix form redirect issue when refresh
    
    all_todos = Todo.objects.all()
    logger.info(f'all todos : {all_todos}')
    todo_page_loader = loader.get_template('tut_app_1/todo.html')
    return HttpResponse(todo_page_loader.render(context = {'todos': all_todos} , request= request))


def delete_todo(request, id):
    logger.info(f'delete data : {id}')
    delete_todo = Todo.objects.get(id = id)
    delete_todo.delete()
    return redirect('/todo/')
    