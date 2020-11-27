from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from auctionItem.models import Contact,Wishlist


# Create your views here.

def register(request):
    if request.method =='POST':
        # messages.add_message(request, messages.ERROR, 'Username taken')
        # return redirect('register')
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exist')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'You are now register,please log in')
                    return redirect('login')
                
        else:
            messages.add_message(request, messages.ERROR, 'Passwords does not match')
            return redirect('register')
            
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request, messages.SUCCESS, 'You have now logged in successfully')
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect('login')
   
    else:
        return render(request,'login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out successfullt')
        return redirect('home-page')
        
        
    return redirect('home-page')

def dashboard(request):
    contact_dashboard=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)  
   
    context={
        'contacts':contact_dashboard
      
    }
    return render(request,'dashboard.html',context)

def wishlist(request):
    contact_wishlist=Wishlist.objects.order_by('-Wishlisted_date').filter(user_id=request.user.id)  
   
    context={
        'wishlists':contact_wishlist
      
    }
    return render(request,'wishlist.html',context)