from django.shortcuts import render
from .models import TaskModel
# Create your views here.
def vazifa_l(request):
    vazifalar = TaskModel.objects.all()
    
    context = {
        "vazifalar": vazifalar
    }
    
    return render(request,'mentorapp/vazifa.html',context)

    
