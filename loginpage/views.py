# from django.contrib import messages
# from django.http.response import HttpResponse
# from django.shortcuts import redirect, render
# #from .models import Details, Userdata
# from django.contrib.auth import authenticate

# # Create your views here.

# def homepage(request):
#     return render(request, 'homepage.html')


# def register(request):

#     if(request.method == 'POST'):
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#         mobile = request.POST['mobile']
#         city = request.POST['city']

#         if Userdata.objects.filter(username=username).exists():
#             #print('Username already taken')
#             messages.info(request,'Username already taken')
#             return redirect('register')
#         elif Userdata.objects.filter(email=email).exists():
#             #print('Email already taken')
#             messages.info(request,'Email already taken')
#             return redirect('register')
#         else:
#             user = Userdata.objects.create(username=username, password=password,firstname=firstname,lastname=lastname,
#                                     email=email,mobile=mobile,city=city)
#             user.save()
#             print('User created')
#             messages.info(request,'Your registration is successful! please click on login')


#         return redirect('/user/homepage')

#     else:
#         return render(request,'register.html')

# def login(request):
#     if(request.method == 'POST'):
#         username = request.POST['username']
#         password = request.POST['password']
# g
#         #if(username == User.objects.get(username=username)):
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#                 login(request, user)
#                 messages.info(request,'Successfully logged in')
#                 return redirect('/user/homepage')
#         else:
#                 messages.info(request,'Invalid Credentials')
#                 return redirect('login')
#         # else:
#         #     messages.info(request,'No such account exists...please register and try again')
#         #     return redirect('/user/homepage')
        
#     else:
#         return render(request,'login.html')








# def display(request):

    # username = request.POST['username']
    # password = request.POST['password']

    # details1 = Details()
    # details1.username = request.POST['username']
    # details1.password = request.POST['password']
    #return render(request, 'logindisplay.html', {'details':details1})

    # details = Details.objects.all()
    # return render(request, 'databaseresult.html', {'details':details})

