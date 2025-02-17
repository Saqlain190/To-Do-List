from django.http import HttpResponse
from django.template import loader
from .forms import SignupForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task



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
            return redirect('/home2')  # Redirect to home page
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'html_record/signin.html')




from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Or whatever template you use for the homepage

def home2(request):
    return render(request, 'index2.html')  # Or whatever template you use for the homepage


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Prevent saving immediately
            task.user = request.user  # Assign the logged-in user to the task
            task.save()  # Save the task
            messages.success(request, "Task has been saved sucessfully !") 
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form})

from django.shortcuts import render
from datetime import date
from .models import Task  # Assuming Task is your model

def view_tasks(request):
    today = date.today()
    
    # Automatically mark tasks as completed if the due date has passed
    Task.objects.filter(due_date__lt=today, completed=False).update(completed=True)

    tasks = Task.objects.all()
    return render(request, 'viewtask.html', {'tasks': tasks, 'today': today})





# def viewtask(request):
#   template = loader.get_template('viewtask.html')
#   return HttpResponse(template.render())html