
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
        fields = '__all__'
        
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
        
class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
    
    
class CreateHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = "__all__"     
        
class CreateHomeworkSubmitionForm(forms.ModelForm):
    class Meta:
        model = HomeworkSubmition
        fields = "__all__"
   
class CreateLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"   
        
class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"   

class CreateExtraMaterialForm(forms.ModelForm):
    class Meta:
        model = ExtraMaterial
        fields = "__all__"   

          
     