
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz ,name='quiz'),
    path('exams', views.exams ,name='exams'),
    path('home', views.home ,name='home'),
    
]