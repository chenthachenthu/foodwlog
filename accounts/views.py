from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

# Create your views here.
from shop.views import home


def registration(request):

    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 =request.POST['password2']
        if username=='':
            messages.info(request,"please enter the username")
            return redirect("registration")

        elif password=='' and password2=='':
            messages.info(request,"please enter the password")
            return redirect("registration")

        else:
            if password==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect("registration")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "email taken")
                    return redirect("registration")
                else:
                    user=User.objects.create_user(username=username,password=password,email=email)
                    user.first_name=firstname
                    user.last_name=lastname
                    user.save()
                    print('Registered')
            else:
                print("password not matched")
                messages.info(request,"password not matched")
                return redirect('registration')
            return redirect('/')
    else:
        return render(request,'registration.html')


def login(request):
    if 'username' in request.session:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            # auth.login(request, user)
            return render(request,'home.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(login)
