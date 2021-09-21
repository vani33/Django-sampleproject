from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if(password1 == password2):
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                employee = User.objects.create_user(username=username,password=password1,first_name=first_name,
                        last_name=last_name,email=email)
                employee.save()
                messages.info(request,'Your Registration is successful...please click below to login')
                return redirect('login')
                
        else:
            messages.info(request,'Password not matched')
            return redirect('register')
        return redirect('homepage')

    else:
        return render(request, "register.html")



def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        employee = auth.authenticate(username=username,password=password)

        if(employee is not None):
            auth.login(request,employee)
            messages.info(request,'Hi ' + employee.username)
            return render(request,"logindisplay.html")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')


    else:
        return render(request,"login.html")