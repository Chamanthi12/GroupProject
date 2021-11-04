from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexView(request):
    return render(request,'index.html')

# @login_required()


def registerView(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password-repeat']

        if(password == password_repeat):
            if(User.objects.filter(username= email).exists()):
                print('User name already taken')
                messages.info(request, 'This Email Already Registerd')
                return render(request,'registration/register.html')
            else:
                user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                return redirect('login.html')
        else:
            print('password does not match')
            messages.info(request, 'Password Does Not Match')
            return render(request,'registration/register.html')

    else:
        return render(request,'registration/register.html')

def loginView(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('Username or Password does not match')
            messages.info(request, 'Username or Password does not match')
            return redirect('login')
    else:
        return render(request,'registration/login.html')