from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def authentication(request):
    return render(request, 'authentication.html')


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("username =",username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('register')

        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('register')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('login')
    return render(request, 'register.html')