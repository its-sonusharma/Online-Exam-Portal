from django.contrib import admin
from . models import Exams
from . models import Question
from . models import Result
# Register your models here.

admin.site.register(Exams)

admin.site.register(Question)

admin.site.register(Result)