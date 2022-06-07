from django.db import models

# Create your models here.
class CourseQuiz(models.Model):
    course_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.course_name
    


class QuestionQuiz(models.Model):
    course = models.ForeignKey(CourseQuiz,on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    option_one = models.CharField(max_length=200)
    option_two = models.CharField(max_length=200)
    option_three = models.CharField(max_length=200,blank=True)
    option_four = models.CharField(max_length=200,blank=True)
    
    answer1 = models.IntegerField()
    
    