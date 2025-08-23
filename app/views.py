from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Contact
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout 
from datetime import datetime

from django.http import HttpResponse

def handleSearch(request):
    if request.method == "POST":
       Searched = request.POST['Searched']
       venues = Venue.objects.filter(name__contains=Searched)
       return render(request, "searchs.html", {"Searched": Searched, "venues": venues})
    else:
        return render(request, "searchs.html")
    


def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        contact = Contact(name=name, subject=subject, phone=phone, email=email, comment=comment)
        contact.save()
        messages.success(request, "Message sent successfully.")
        return redirect('contact')

    return render(request, 'Contact.html')

def handleSignUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Password match check
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect("index")

        # Username already exists?
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return redirect("index")

        # Email already exists? (optional)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please log in.")
            return redirect("index")

        # Create the user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect("index")

    else:
        return redirect("index")
    
def handleLogin(request):    
       if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In ")
            return redirect("index")
        else:
            messages.error(request,"Invalid Inputs , Please Try Again ")
            return redirect("index")

    
        
def handleLogout(request):
   logout(request)
   messages.success(request, "You Are Successfully Logged Out")
   return redirect("index")
