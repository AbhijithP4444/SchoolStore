from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request, "form.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

                user.save();

                return redirect('login')


        else:
            messages.info(request, "password not matching")
            return redirect('register')

        return redirect('/')

    return render(request, "register.html")

def formfill(request):
    if request.method == 'POST':
        messages.info(request, "Order Placed")
        return redirect('formfill')


    return render(request,"formfill.html")






# Create your views here.
