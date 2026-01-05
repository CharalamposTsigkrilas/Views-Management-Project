from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    error = None
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
        error = 'Λάθος στοιχεία'

    return render(request, 'accounts/login.html', {'error': error})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    error = None
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            error = 'Το username υπάρχει ήδη'
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/signup.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')