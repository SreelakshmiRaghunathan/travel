from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd = request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        pwd2 = request.POST['pwd2']


        if pwd==pwd2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username is already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)
                user.save();
                return  redirect('login')

        else:
            messages.info(request,"Password is not matching")
            return redirect('register')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')