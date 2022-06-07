from django.db import models





GENDER = [
    ("Male" , "Male"),
    ("Female", "Female")

    ]

class Course(models.Model):
    title = models.CharField(max_length= 55)
    price = models.PositiveIntegerField()
    description = models.TextField()
    lesson_qty = models.PositiveIntegerField()
    datee = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
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
    


    