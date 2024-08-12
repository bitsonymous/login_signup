from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home_view(request):
    # if not request.user.is_authenticated:
    #   return redirect('login')
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      print(user)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        return HttpResponse( "Invaild Details")
  
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect('signup')
        
        my_user = User.objects.create_user(username, email, password)
       
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')
