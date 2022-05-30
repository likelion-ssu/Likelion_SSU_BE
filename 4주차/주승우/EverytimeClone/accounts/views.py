from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(request):
    if request.method == 'POST':
        userId = request.POST['userid']
        password = request.POST['password']
        user = authenticate(request, username=userId, password=password)

        if user:
            auth_login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user = User()
        if request.POST['password'] == request.POST['confirmPassword']:
            user.username = request.POST['userid']
            user.set_password(request.POST['password'])
            user.nickname = request.POST['nickname']
            user.save()
            return redirect('login')
        return render(request, 'register.html')
    return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    return redirect('main')

    
