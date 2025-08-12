from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Contact
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

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


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('index')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('index')

        user = User.objects.create_user(username=username, email=email, password=pass1)
        user.save()
        messages.success(request, "Signup successful! You can now login.")
        return redirect('index')

    return render(request, 'index.html')




def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('index')

    return render(request, 'index.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')