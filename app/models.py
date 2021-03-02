from django.db import models

# Create your models here.
class Exams(models.Model):
    exam_name = models.CharField(max_length=50)
    no_of_ques = models.CharField(max_length=20)
    total_marks = models.CharField(max_length=20)
    time_duration = models.DurationField(default='00:00:00')
    def __str__(self):
        return str(self.exam_name)

class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    exam_name = models.ForeignKey(Exams, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=0)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    choose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
    answer = models.CharField(max_length=1, choices=choose)
    def __str__(self):
        return str(self.question)


class Result(models.Model):
    exam_name = models.ForeignKey(Exams, on_delete=models.CASCADE)
    no_ques_attempt = models.Count
    no_ques_unattempt = models.Count
    no_ques_right = models.Count
    no_ques_wrong = models.Count
    total_mark = models.Count
