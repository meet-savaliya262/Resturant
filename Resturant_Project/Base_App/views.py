from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import BookTable,AboutUs,Feedback,ItemList,Items
# Create your views here.

def HomeView(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    review=Feedback.objects.all()
    return render(request,'index.html',{'items':items,'list':list,'review':review})

def AboutView(request):
    return render(request,'about.html')


def MenuView(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    return render(request,'menu.html',{'items':items,'list':list})


def BookTableView(request):
    return render(request,'book_table.html')

def Feedbacks(request):
    return render(request,'feedback.html')