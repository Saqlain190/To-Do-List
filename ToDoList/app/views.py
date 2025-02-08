from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect



User = get_user_model()

def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        


        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')
        
        
        # Save the user
        user = User.objects.create_user(
            username=user_name,
            email=email,
            password=password,
        )
        user.save()


        messages.success(request, "Signup successful!")
        return redirect('signup')  # Redirect to a success or login page

    return render(request, 'html_record/signup.html')




@csrf_protect
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Get the username from the email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return render(request, 'html_record/signin.html')

        # Authenticate the user using their email
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('/home')  # Redirect to home page
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'html_record/signin.html')




def member(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


# def signin(request):
#   template = loader.get_template('signin.html')
#   return HttpResponse(template.render())


# def addtask(request):
#   template = loader.get_template('addtask.html')
#   return HttpResponse(template.render())


# def viewtask(request):
#   template = loader.get_template('viewtask.html')
#   return HttpResponse(template.render())