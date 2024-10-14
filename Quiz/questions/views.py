from django.shortcuts import render
from .models import *


def quiz(request):
    context ={
        'exam' : Exam.objects.all(),
    }
    return render(request,'pages/quiz.html' ,context)

def exams(request):
    return render(request,'pages/exams.html')
def home(request):
    return render(request,'pages/home.html') 