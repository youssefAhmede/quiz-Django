from django.db import models

class Exam(models.Model):
    question_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, null=True, blank=True)
    question_mark = models.IntegerField(null=True, blank=True)
    question = models.TextField(max_length=1000)
    option1 = models.CharField(max_length=100, null=True, blank=True)
    option2 = models.CharField(max_length=100, null=True, blank=True)
    option3 = models.CharField(max_length=100, null=True, blank=True)
    option4 = models.CharField(max_length=100, null=True, blank=True)
    correct = models.CharField(max_length=100, null=True, blank=True)

