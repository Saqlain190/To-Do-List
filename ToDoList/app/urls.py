from django.contrib import admin
from django.urls import path
from . import views
from app.views import signin, signup
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/',views.member),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    # path('addtask/',views.addtask),
    # path('viewtask/',views.viewtask),
    
    
]