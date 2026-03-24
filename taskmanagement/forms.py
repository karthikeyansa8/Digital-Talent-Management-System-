from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from taskmanagement.models import Task


class RegistrationForm(forms.ModelForm):
    
    first_name = forms.CharField(label='first_name', max_length=20, required=True)
    last_name = forms.CharField(label='last_name', max_length=20, required=True)
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', min_length=6, required=True)
    confirm_password = forms.CharField(label='confirm_password',min_length=6, required=True)
    
    
    def clean(self):
        cleaned_data =  super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        # username = cleaned_data.get('first_name') + cleaned_data.get('last_name')
        # print(first_name,last_name,email,password,confirm_password)

        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Exists")
        
        if password and confirm_password and password!=confirm_password:
            raise forms.ValidationError("Password and Confirm password does not match")
        
        return cleaned_data
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        
        
class LoginForm(forms.Form):
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', min_length=6, required=True)
    
    def clean(self):
        cleaned_data =  super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        print(email,password)
        
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email does not exist")
        
        return cleaned_data
    
class AdminLoginForm(forms.Form):
    email = forms.EmailField(label='email', required=True)
    password = forms.CharField(label='password', min_length=6, required=True)
    
    def clean(self):
        cleaned_data =  super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        print(email,password)
        
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email does not exist")
        
        user = authenticate(username=email,password=password)
        if user is not None and not user.is_staff:
            raise forms.ValidationError("You are not authorized to access admin panel")
        
        return cleaned_data
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='email', required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email does not exist")
        
        return cleaned_data
    

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='new_password', min_length=6, required=True)
    confirm_password = forms.CharField(label='confirm_password',min_length=6, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if new_password and confirm_password and new_password!=confirm_password:
            raise forms.ValidationError("New password and Confirm password does not match")
        
        return cleaned_data
    
    
class TaskForm(forms.ModelForm):
    title = forms.CharField(label='title', max_length=100, required=True)
    description = forms.CharField(label='description', widget=forms.Textarea, required=True)
    task_link = forms.URLField(label='task_link', required=True)
    
    class Meta:
        model = Task
        fields = ['title','description','task_link']
        
   