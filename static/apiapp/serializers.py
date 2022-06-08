from rest_framework import serializers
from testapp.models import * 

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
class MenteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentee
        fields = '__all__'
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_dars
        fields = '__all__'
        
        
        