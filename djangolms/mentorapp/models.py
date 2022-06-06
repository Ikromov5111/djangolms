from django.db import models
from testapp.models import Group,Mentor

# Create your models here.
class TaskModel(models.Model):
    task_name = models.CharField(max_length=100)
    file= models.FileField(upload_to='media/')
    group = models.ForeignKey("testapp.Group", on_delete=models.CASCADE)
    dedlayn = models.DateTimeField()
    username = models.OneToOneField('testapp.Mentor',primary_key=True,on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.task_name
    
    