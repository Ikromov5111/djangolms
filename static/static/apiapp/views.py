from django.shortcuts import render
from .serializers import *
from testapp.models import * 
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ViewSet
from .pagination import CoursePageNumberPagination
# Create your views here.

class CourselistApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePageNumberPagination
    
    
class MentorListCreateApiView(ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    pagination_class = CoursePageNumberPagination
    
class GroupListCreateApiView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CoursePageNumberPagination
    
class MenteeListCreateApiView(ListCreateAPIView):
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer
    pagination_class = CoursePageNumberPagination

class CoursesuperApiView(RetrieveUpdateDestroyAPIView):
    queryset = Course
    serializer_class = CourseSerializer
    
class MentorsuperApiView(RetrieveUpdateDestroyAPIView):
    queryset = Mentor
    serializer_class = MentorSerializer
    
class GroupSuperApiView(RetrieveUpdateDestroyAPIView):
    queryset = Group
    serializer_class = GroupSerializer
    
class MenteeSuperApiView(RetrieveUpdateDestroyAPIView):
    queryset = Mentee
    serializer_class = MenteeSerializer
    
    
    
