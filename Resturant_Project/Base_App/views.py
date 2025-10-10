from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Base_App.models import BookTable,AboutUs,Feedback,ItemList,Items,Order
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomeView(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    review=Feedback.objects.all()
    return render(request,'index.html',{'items':items,'list':list,'review':review})

@login_required(login_url='login')
def AboutView(request):
    data=AboutUs.objects.all()
    return render(request,'about.html',{'data':data})

@login_required(login_url='login')
def MenuView(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    return render(request,'menu.html',{'items':items,'list':list})

@login_required(login_url='login')
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

@login_required(login_url='login')
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


def add_to_cart(request, food_id):
    item = get_object_or_404(Items, id=food_id) 
    cart = request.session.get('cart', {})

    if str(item.id) in cart:
        cart[str(item.id)]['quantity'] += 1
    else:
        cart[str(item.id)] = {
            'name': item.Item_name, 
            'price': item.Price,
            'quantity': 1,
            'image': item.Image.url
        }
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart_view')


def increase_quantity(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    request.session['cart'] = cart
    return redirect('cart_view')  

def decrease_quantity(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        if cart[str(item_id)]['quantity'] > 1:
            cart[str(item_id)]['quantity'] -= 1
        else:
            cart[str(item_id)]['quantity'] = 1
    request.session['cart'] = cart
    return redirect('cart_view')



def remove_from_cart(request, food_id):
    cart = request.session.get('cart', {})
    if str(food_id) in cart:
        del cart[str(food_id)]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart_view')

@login_required(login_url='login')
def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})



def Login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request,"Invalid username")
            return redirect('login')
        
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Invalid username/password")
            return redirect('login')
        else:
            login(request,user)
            return redirect('/')


    return render(request, 'login.html')


def Signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"username already exist")
            return redirect('signup')
        
        user=User.objects.create(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account created successfully")
        return redirect('login')
    return render(request, 'signup.html')

def Logout_page(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart_view')

    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'checkout.html', {'cart': cart, 'total': total})


@login_required(login_url='login')
def place_order(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('cart_view')

        total = sum(item['price'] * item['quantity'] for item in cart.values())

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Save order
        order = Order.objects.create(
            user=request.user,
            name=name,
            email=email,
            phone=phone,
            address=address,
            total_amount=total
        )

        for item_id, item_data in cart.items():
            item = Items.objects.get(id=item_id)
            order.food_items.add(item)

        request.session['cart'] = {}
        request.session.modified = True

        return redirect('order_success')

    return redirect('checkout')



@login_required(login_url='login')
def order_success(request):
    return render(request, 'success.html')
