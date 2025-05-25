from django.urls import path
from . import views


urlpatterns = [
    path("", views.welcome_page, name="welcome_page"),
    path("home/", views.home_page, name="home_page"),
    path("questions/", views.questions_page, name="question_page"),
    path('todo/', views.todo_page, name='todo_page'),
    
    path('delete/<id>', views.delete_todo, name='delete_todo')
]