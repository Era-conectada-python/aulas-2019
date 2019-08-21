from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question, Choice


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def questions(request):
    questions = list(Question.objects.all().values('id', 'question_text'))

    for question in questions:
        question['choices'] = list(Choice.objects.filter(question=question['id']).values('choice_text'))
    
    return render(request, 'template/questions.html', {'questions': questions})
