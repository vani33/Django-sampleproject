from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Vani'})

def add(request):

    # val1 = int(request.GET['number1'])
    # val2 = int(request.GET['number2'])

    val1 = int(request.POST['number1'])
    val2 = int(request.POST['number2'])

    res = val1 + val2

    return render(request,'result.html', {'result':res})