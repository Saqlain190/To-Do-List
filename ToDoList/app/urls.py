from django.contrib import admin
from django.urls import path
from . import views
from app.views import signin, signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/',views.home),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('add/', views.add_task, name='add_task'),
    path('tasks/', views.view_tasks, name='view_tasks'),
    path('home2/', views.home2 ),

    
]