from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('home', views.index, name = 'home'),
    path('blog',views.blog,name = 'blog'),
    path('courses', views.courses, name = 'courses'),
    path('register', views.register, name ='register'),
    path('login',views.login,name='login'),
    path('contact',views.contact, name = 'contact'),
    path('logout',views.logout,name = 'logout'),
    path('exam',views.exam,name ='exam'),
    path('result',views.result,name ='result'),
    path('c_exam',views.c_exam,name ='c_exam'),
    path('c_result',views.c_result,name ='c_result'),
]