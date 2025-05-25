from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length= 200)
    votes = models.IntegerField(default= 0)
    
    def __str__(self):
        return self.choice_text
    
    
class Todo(models.Model):
    task_text = models.CharField(max_length= 100)
    created_date = models.DateField('created date')
    
    def __str__(self):
        return f'task:= {self.task_text} created at: {self.created_date}'