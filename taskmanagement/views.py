from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.models import User
def register(request):
    
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Set username to email
            user.username = form.cleaned_data['email']
            
            #password Hashing
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Registered Successfully! Now you can login')
            return redirect(reverse('login'))
        
        
    return render(request,'register.html',{'form':form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request,username=email,password=password)
            print("user:",user) #--> gives the username eg:karthi39
            
            if user is not None:
                auth_login(request,user)
                print('Successfully Login!')
                messages.success(request,'Login Successfully!')
                return redirect(reverse('main'))
    return render(request,'login.html',{'form':form})


def main(request):
    return render(request,'main.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect(reverse('login'))