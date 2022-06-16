from django.urls import path
from . import views
urlpatterns = [
    
    #path("",views.mainpage,name = 'mainpage'),
    path("" , views.dashboard, name = 'dashboard'),
    path("test/", views.test, name = 'test'),   
    
    path('login/', views.loginuser, name = 'login'),
    path('logout/', views.logoutuser, name = 'logout'),
    path('register/', views.register_user, name = 'register') , 
          
    path('course_c/' ,views.course_create, name = 'course_c') ,         
    path('course_t/' ,views.course_t, name = 'course_t') ,
    path("course_u/<str:pk>", views.course_u, name = "course_u"),
    path("course_del/<str:pk>", views.course_d, name = "course_d"),
    
    path("mentor_c/" , views.mentor_c, name= 'mentor_c'),
    path("mentor_t/" , views.mentor_t,name= 'mentor_t'),
    path("mentor_u/<str:pk>",views.mentor_u, name= 'mentor_u'),
    path("mentor_d/<str:pk>", views.mentor_d,name = "mentor_d"),
    
    path("group_c/", views.group_c , name = "group_c"),
    path("group_t/", views.group_t , name = "group_t"),
    path("group_u/<str:pk>", views.group_u , name = "group_u"),
    path("group_d/<str:pk>", views.group_d, name = "group_d"),
    
    path("mentee_c/", views.mentee_c , name="mentee_c"),
    path("mentee_t/", views.mentee_t, name="mentee_t"),
    path("mentee_d/<str:pk>", views.mentee_d,name="mentee_d"),
    path("mentee_u/<str:pk>", views.mentee_u,name="mentee_u"),
    
    path("lesson-c/",views.lesson_c, name= "lesson_c"),
    path("lesson-t/", views.lesson_t,name = "lesson_t"),
    path("lesson-u/<int:pk>",views.lesson_u, name = 'lesson_u'),
    path("lesson-d/<int:pk>", views.lesson_d, name = "lesson_d"),
    
    path("homework-c/",views.homework_c, name= "homework_c"),
    path("homework-t/", views.homework_t,name = "homework_t"),
    path("homework-u/<int:pk>",views.homework_u, name = 'homework_u'),
    path("homework-d/<int:pk>", views.homework_d, name = "homework_d"),
    
    path("homeworksubmition-c/",views.homeworksubmition_c, name= "homeworksubmition_c"),
    path("homeworksubmition-t/", views.homeworksubmition_t,name = "homeworksubmition_t"),
    path("homeworksubmition-u/<int:pk>",views.homeworksubmition_u, name = 'homeworksubmition_u'),
    path("homeworksubmition-d/<int:pk>", views.homeworksubmition_d, name = "homeworksubmition_d"),
    
    path("video-dars/", views.video_dars , name = "video_dars" ),
    path("video-c/",views.video_list, name = "video_c"),
    ]