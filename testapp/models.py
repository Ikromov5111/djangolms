from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth import get_user




GENDER = [
    ("Male" , "Male"),
    ("Female", "Female")

    ]

class Course(models.Model):
    title = models.CharField(max_length= 55)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='UZS')
    description = models.TextField()
    lesson_qty = models.PositiveIntegerField()
    datee = models.DateTimeField(auto_now_add = True)
    academy_portion = models.IntegerField()

    def __str__(self):
        return self.title
    
    @property
    def mentor_portion(self):
        return (100-self.academy_portion)
    
class Mentor(models.Model):
  
    full_name = models.CharField(max_length = 100)
    birth_date = models.DateField()
    gender = models.CharField(max_length = 6, choices=GENDER, default = 'Male')
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    specification = models.CharField(max_length= 50)
    datee = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

class Group(models.Model):
    title =  models.CharField(max_length = 50)
    course = models.ForeignKey(Course, on_delete= models.SET_NULL, blank = True , null = True )
    mentor = models.ForeignKey(Mentor, on_delete= models.SET_NULL, blank= True , null = True)
    datee = models.DateTimeField(auto_now_add=True)
    student_qty = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    def group_total_price(self):
        group_total_price =self.course.price *  self.student_qty 
        return group_total_price
    
    def center_income(self):
        return self.student_qty * self.course.academy_portion
    
    def mentor_income(self):
        return self.student_qty * self.course.mentor_portion        


class Mentee(models.Model):
    PAYMENT = [
        ('paid' , 'paid'),
        ('unpaid', 'unpaid')
    ]
    full_name = models.CharField(max_length= 100)
    birth_date = models.DateField()
    gender = models.CharField(max_length = 6 , choices= GENDER , default = "Male")
    phone = models.CharField(max_length = 13)
    email = models.EmailField()
    address = models.CharField(max_length = 50)
    group = models.ForeignKey(Group,on_delete = models.SET_NULL,blank = True, null = True)
    payment = models.CharField(max_length =6 , choices= PAYMENT, default = 'unpaid' )
    datee = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.full_name


class Video_dars(models.Model):
    video_url = models.URLField()
    title = models.CharField(max_length=50)
    for_group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)
    birinchi_kirish = models.DateTimeField(auto_now_add = True)
    
    
    
class Blog(models.Model):
    title = models.CharField(max_length=55)
    photo = models.ImageField(upload_to="media")
    author = models.CharField(max_length=88)
    description = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Lesson(models.Model):
    STATUS={
         ("Planned", "Planned"),
        ("Completed", "Completed"),
        ("Canceled", "Canceled")
    }
    
    group = models.ForeignKey(Group,on_delete=models.SET_NULL,null = True, blank=True)
    author = models.CharField(max_length=60)
    lesson_num = models.PositiveIntegerField()
    topic = models.CharField(max_length=150)
    added_time = models.DateTimeField(auto_now_add=True)
    zoom_link = models.URLField(null=True,blank=True)
    file = models.FileField(upload_to = "media",null=True,blank=True)
    lesson_status = models.CharField(max_length=11,choices=STATUS,default="Planned")
    
    
    def __str__(self):
        return self.topic
    
        
class Homework(models.Model):
    group = models.ForeignKey(Group,on_delete=models.SET_NULL,blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null=True)
    task = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    

    def __str__(self):
        return str(self.lesson)
    
    
class HomeworkSubmition(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.SET_NULL, blank=True, null=True)
    link = models.URLField(max_length = 500)
    information = models.TextField(blank=True, null=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    homework_file = models.FileField(upload_to="media")

    def __str__(self):
        return str(self.homework)

class ExtraMaterial(models.Model):
    # course = models.ForeignKey(Group, on_delete=SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True,blank=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)
    # lesson_num = models.ForeignKey(Lesson, on_delete=SET_NULL, null=True)
    title = models.CharField(max_length=300)
    youtube_link = models.URLField(max_length = 500)
    presentation = models.FileField(upload_to='media', blank="True", null="True")
    text_content = models.TextField()

    def __str__(self):
        return self.title

class Message(models.Model):
    sender_name = models.CharField(max_length=50)
    message_content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    message_receiver = models.CharField(max_length=55)
    def __str__(self):
        return self.id