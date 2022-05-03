from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator



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
    return render(request, 'mainapp/dashboard.html')

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
    
    return render(request,'manapp/group_table.html',context)


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



