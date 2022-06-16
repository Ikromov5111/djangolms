from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator
from .models import *
from datetime import date



def video_dars(request):
    videos = Video_dars.objects.all()
    paginator = Paginator(videos, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "videos" : videos,
        "page_obj" : page_obj,
    }
    return render(request,'mainapp/video_dars.html',context)  
    
def video_list(request):
    return render(request,'mainapp/vidyo_yuklash.html')

# Create your views here.
#def mainpage(request):
   # return render(request , "mainapp/index.html")
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username = username,password = password)
            
            if user is not None:
                login(request,user)
                return redirect("dashboard")
            else:
                messages.info(request,"Qandaydir xatolik:")
        context={}
        return render(request,'mainapp/login.html',context)
    
@login_required(login_url = "login")       
def logoutuser(request):
    logout(request)
    return redirect("login")        

@login_required(login_url = 'login')
def dashboard(request):
    student_qty = Mentee.objects.all().count()
    course_qty = Course.objects.all().count()
    groups = Group.objects.all()
    system_user_qty = User.objects.all().count()
    today = date.today()
    full_income = 0
    
    for group in groups:
        full_income += group.group_total_price()
        
    context = {
        "student_qty":student_qty,
        "course_qty":course_qty,
        "full_income":full_income,
        "system_user_qty":system_user_qty,
        "today":today
    }
    return render(request, 'mainapp/dashboard.html',context)

def register_user(request):
    form = CreatedUserForm()
    if request.method == "POST":
        form = CreatedUserForm(request.POST)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get("username")
            return redirect('login')
    context = {
        "form":form
    }
    return render(request, 'mainapp/register.html', context)

def test(request):
    return render(request , 'mainapp/temp.html')

@login_required(login_url='login')
def course_create(request):
    if request.user.is_superuser:
        form = CreateCourseForm()
        if request.method == "POST":
            form = CreateCourseForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('course_t')
            else:
                form = CreateCourseForm()

        context = {
            "form" : form
        }
        return render(request,'mainapp/created_course.html', context)
    else:
        return redirect('dashboard')
    
@login_required(login_url = 'login')    
def course_t(request):
    if request.user.is_superuser:
        courses = Course.objects.all()
        context = {
            "courses" :courses
        }
        return render(request,'mainapp/course_table.html' , context)
    else :
        return redirect("dashboard")
@login_required(login_url = 'login')
def course_u(request,pk):
    if request.user.is_superuser:
         
        course= Course.objects.get(id = pk)
        form = CreateCourseForm(instance = course)
        if request.method == "POST":
            form = CreateCourseForm(request.POST,instance=course)
            if form.is_valid:
                form.save()
                return redirect('course_t')
        
        context = {
            "form" : form
        }
        
        return render(request,'mainapp/created_course.html', context)
    else :
        return redirect("dashboard")
@login_required(login_url = 'login')
def course_d(request,pk):
    if request.user.is_superuser:
        
        course = Course.objects.get(id = pk)
        if request.method == 'POST':
            course.delete()
            return redirect("course_t")
        context = {
            "course" : course
        }
        return render(request,'mainapp/course_delete.html' , context)
    else :
        return redirect('dashboard')


@login_required(login_url = 'login')
def mentor_c(request):
    if request.user.is_superuser:
        form = CreateMentorForm()
        if request.method == "POST":
            form = CreateMentorForm(request.POST)
            if form.is_valid:
                form.save()
                
                return redirect("mentor_t")
            else:
                form = CreateMentorForm()
        context = {
            "form" : form
        }
    
        return render(request,'mainapp/mentor_create.html',context)
    else:
        return redirect('dashboard')
@login_required(login_url = 'login')
def mentor_t(request):
    if request.user.is_superuser:
        mentors = Mentor.objects.all().order_by("full_name")
        context = {
            "mentors" : mentors
        }
        
        return render(request,'mainapp/metor_table.html',context)
    else: 
        return redirect('dashboard')
@login_required(login_url = 'login')
def mentor_u(request,pk):
    if request.user.is_superuser:
        mentor = Mentor.objects.get(id=pk)
        form = CreateMentorForm(instance=mentor)
        if request.method == "POST":
            form = CreateMentorForm(request.POST, instance=mentor)
            if form.is_valid:
                form.save()
                return redirect('mentor_t')   
        
        context = {
            "form" : form
        } 
        
        return render(request,'mainapp/mentor_create.html',context)
    else :
        return redirect("dashboard")
@login_required(login_url = 'login')
def mentor_d(request,pk):
    if request.user.is_superuser:
        mentor= Mentor.objects.get(id = pk)
        if request.method == "POST":
            mentor.delete()
            return redirect("mentor_t")
        context = { 
            "mentor" : mentor
        }
        
        return render(request,'mainapp/mentor_delete.html', context)
    else:
        return redirect("dashboard")


def group_c(request):
    if request.user.is_superuser:
        form = CreateGroupForm()
        if request.method == "POST":
            form = CreateGroupForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('group_t')
            else:
                form = CreateGroupForm()
                
        context = {
            "form" : form
        }
        return render(request,'mainapp/group_c.html', context)
    else:
        return redirect("dashboard")

def group_t(request):
    groups = Group.objects.all().order_by("title")
    context = {
        "groups" : groups
    }
    return render(request,'mainapp/group_table.html',context)

def group_u(request,pk):
    group = Group.objects.get(id = pk)
    form = CreateGroupForm(instance = group)
    if request.method == "POST":
        form= CreateGroupForm(request.POST, instance = group)
        if form.is_valid:
            form.save()
            return redirect('group_t')
    
    context = {
        "form" : form
    }
    
    return render(request,'mainapp/group_c.html' , context)
        
def group_d(request,pk):
    group = Group.objects.get(id = pk )  
    if request.method == "POST":
        group.delete()     
        return redirect("group_t")
    context = {
        "group" : group
    } 
    
    return render(request,'mainapp/group_delete.html',context)


def mentee_c(request):
    form = CreateMenteeForm()
    if request.method == "POST":
        form = CreateMenteeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('mentee_t')
        else :
            form = CreateMenteeForm()
            
    context = {
        "form" : form
    }
    
    return render(request,'mainapp/mentee_create.html', context)

def mentee_t(request):
    mentees = Mentee.objects.all()
    context = {
        "mentees" : mentees
    }
    return render(request, 'mainapp/mentee_table.html', context)

def mentee_u(request,pk):
    mentee = Mentee.objects.get(id = pk)
    form = CreateMenteeForm(instance = mentee)
    if request.method == "POST":
        form = CreateMenteeForm(request.POST,instance = mentee)
        if form.is_valid:
            form.save()
            return redirect('mentee_t')
        
    context = {
        "form" : form
    }
    
    return render(request, 'mainapp/mentee_create.html' , context)


def mentee_d(request,pk):
    mentee = Mentee.objects.get(id= pk)
    if request.method == "POST":
        mentee.delete()
        return redirect('mentee_t')
    
    context = {
        "mentee" : mentee
    }
    
    return render(request, 'mainapp/mentee_delete.html', context)


def lesson_c(request):
    form = CreateLessonForm()
    if request.method == "POST":
        form = CreateLessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_t')
        else :
            form = CreateLessonForm()
            
    context = {
        "form":form
    }
    
    return render(request,'testapp/lesson_c.html',context)

def lesson_t(request):
    lessons = Lesson.objects.all().order_by(("-id"))
    context = {
        "lessons":lessons
    }
    return render(request,"testapp/lesson_t.html",context)

def lesson_u(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = CreateLessonForm(instance=lesson)
    if request.method == "POST":
        form = CreateLessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_t')
        else :
            form = CreateLessonForm(instance=lesson)
            
    context = {
        "form" : form,
        "lesson" : lesson
    }
    
    return render(request,'testapp/lesson_c.html',context)
  
  
def lesson_d(request,pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == "POST":
        lesson.delete()   
        return redirect("lesson_t")   
    context ={
        "lesson": lesson
        }
    return render(request,"testapp/lesson_d.html",context)
    
    
def homework_c(request):
    form = CreateHomeworkForm()
    if request.method == "POST":
        form = CreateHomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homework_t')
        else :
            form = CreateHomeworkForm()
            
    context = {
        "form":form
    }
    
    return render(request,'testapp/homework_c.html',context)

def homework_t(request):
    homework = Homework.objects.all().order_by(("-id"))
    context = {
        "homework":homework
    }
    return render(request,"testapp/homework_t.html",context)

def homework_u(request, pk):
    homework = Homework.objects.get(id=pk)
    form = CreateHomeworkForm(instance=homework)
    if request.method == "POST":
        form = CreateHomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homework_t')
        else :
            form = CreateHomeworkForm(instance=homework)
            
    context = {
        "form" : form,
        "homework" : homework
    }
    
    return render(request,'testapp/homework_c.html',context)
  
  
def homework_d(request,pk):
    homework = Homework.objects.get(id=pk)
    if request.method == "POST":
        homework.delete()   
        return redirect("homework_t")   
    context ={
        "homework": homework
        }
    return render(request,"testapp/homework_d.html",context)
    
    
def homeworksubmition_c(request):
    form = CreateHomeworkSubmitionForm()
    if request.method == "POST":
        form = CreateHomeworkSubmitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeworksubmition_t')
        else :
            form = CreateHomeworkSubmitionForm()
            
    context = {
        "form":form
    }
    
    return render(request,'testapp/homeworksubmition_c.html',context)

def homeworksubmition_t(request):
    homeworksubmitions = HomeworkSubmition.objects.all().order_by(("-id"))
    context = {
        "homeworksubmitions":homeworksubmitions
    }
    return render(request,"testapp/homeworksubmition_t.html",context)

def homeworksubmition_u(request, pk):
    homework = HomeworkSubmition.objects.get(id=pk)
    form = CreateHomeworkSubmitionForm(instance=homework)
    if request.method == "POST":
        form = CreateHomeworkSubmitionForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homeworksubmition_t')
        else :
            form = CreateHomeworkSubmitionForm(instance=homework)
            
    context = {
        "form" : form,
        "homework" : homework
    }
    
    return render(request,'testapp/homeworksubmition_c.html',context)
  
  
def homeworksubmition_d(request,pk):
    homeworksubmition = HomeworkSubmition.objects.get(id=pk)
    if request.method == "POST":
        homeworksubmition.delete()   
        return redirect("homeworksubmition_t")   
    context ={
        "homeworksubmition": homeworksubmition
        }
    return render(request,"testapp/homeworksubmition_d.html",context)
    
    
