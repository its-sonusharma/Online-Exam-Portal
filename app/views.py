from django.shortcuts import render , redirect
from django.http import HttpResponse 
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Exams,Question,Result

# Create your views here.

def index(request):
    return render (request ,'index.html' )

def home(request):
    return render (request ,'index.html' )

def blog(request):
    return render (request ,'blog.html')

def courses(request):
    return render (request,'courses.html')

@login_required(login_url='login')
def exam(request):

    exam = Exams.objects.all()
    
    ques = Question.objects.filter(exam_name_id = 8).order_by('id')
    
    
    return render (request ,'exam.html', {'exam' : exam , 'ques' : ques  })
    
def result(request):

    exam = Exams.objects.all()

    ques = Question.objects.all()

    return render (request ,'result.html',{'exam' : exam , 'ques' : ques })

@login_required(login_url='login')
def c_exam(request):

    exam = Exams.objects.all()
    
    ques = Question.objects.filter(exam_name_id = 1).order_by('id')
    
    
    return render (request ,'exam.html', {'exam' : exam , 'ques' : ques  })
    
def c_result(request):

    exam = Exams.objects.all()

    ques = Question.objects.filter(exam_name_id = 1).order_by('id')

    return render (request ,'result.html',{'exam' : exam , 'ques' : ques })


def register(request):

    if request.method == 'POST':
    
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']
        
        if password == password_confirm:

            if User.objects.filter(username=username).exists():
                messages.info(request,'username is taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username = username, password = password,email = email,first_name = first_name,last_name = last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,' paassord not matching')
            return redirect('register')    
        
        return redirect('/')

    else:
        return render (request ,'register.html' )    

def login(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid user details')
            return redirect('/')    



    return render (request , 'login.html' )

def contact(request):
    return render (request , 'contact.html' )    

def logout(request):
    auth.logout(request)
    return redirect('/')

  