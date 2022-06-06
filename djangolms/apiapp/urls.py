from django.urls import path
from .views import *
urlpatterns = [
    path("course-list-create/", CourselistApiView.as_view()),
    path("mentor-list-create/", MentorListCreateApiView.as_view()),
    path("group-list-create/", GroupListCreateApiView.as_view()),
    path("mentee-list-create/", MentorListCreateApiView.as_view()),
    
    path("course-super/<int:pk>", CoursesuperApiView.as_view()),
    path("mentor-super/<int:pk>", MentorsuperApiView.as_view()),
    path("group-super/<int:pk>", GroupSuperApiView.as_view()),
    path("mentee-super/<int:pk>", MenteeSuperApiView.as_view() ),



]