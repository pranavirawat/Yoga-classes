from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserAuth, UserProfile
from django.template import loader
from django.shortcuts import render

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'password123':
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials!")
    return render(request, "login_page.html")


def home(request):  
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        goal = request.POST.getlist('goal')
        days = request.POST.get('days')

        user_data = UserProfile(name=name, gender=gender, goal=', '.join(goal), days=days)
        user_data.save()
        return HttpResponse("Registration successful!")

    # Handle GET request: show the form
    return render(request, "register.html") 


from django.http import HttpResponse

def yoga(request):
    return HttpResponse("<h1>Welcome to the Yoga Home Page</h1>")

#def yoga(request):
  #  return render(request, 'yoga/home.html')