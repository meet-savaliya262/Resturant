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
    data=AboutUs.objects.all()
    return render(request,'about.html',{'data':data})


def MenuView(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    return render(request,'menu.html',{'items':items,'list':list})


def BookTableView(request):
    if request.method=='POST':
        name=request.POST.get('user_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        total_person=request.POST.get('total_person')
        booking_date=request.POST.get('booking_date')
        
        if name != '' and phone_number != '' and email != '' and total_person != '' and booking_date != '':
            data=BookTable(Name=name,Phone_number=phone_number,Email=email,Total_person=total_person,Booking_date=booking_date)
            data.save()
    return render(request,'book_table.html')

def Feedbacks(request):
    if request.method=='POST':
        name=request.POST.get('user_name')
        description=request.POST.get('Description')
        rating=request.POST.get('Rating')
        image=request.FILES.get('Image')

        if name != '' and description != '' and rating != '' and image != '':
            data=Feedback(User_name=name,Description=description,Rating=rating,Image=image)
            data.save()
    return render(request,'feedback.html')