from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomeView(request):
    return render(request,'index.html')

def AboutView(request):
    return render(request,'about.html')


def MenuView(request):
    return render(request,'menu.html')


def BookTableView(request):
    return render(request,'book_table.html')

def Feedback(request):
    return render(request,'feedback.html')