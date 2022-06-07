
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class CreatedUserForm(UserCreationForm):
    model = User
    fields = ["username" , "email", "password1", "password2"]
    
class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'price', 'description', 'lesson_qty']
        
class CreateMentorForm(forms.ModelForm):
    
    class Meta:
        model = Mentor
        fields = '__all__'
    
class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        
        
class CreateMenteeForm(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = "__all__"