from django.urls import path
from .views import courseView , take_quiz, api_question
urlpatterns = [
    path("course-v/" , courseView, name = "quiz-home"),
    path("<id>", take_quiz , name = "take-quiz"),
    path("api-quiz/<int:pk>", api_question, name= "api_question" )
    
]
