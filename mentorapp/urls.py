from django.urls import path
from .views import *
urlpatterns = [
    
    path("vazifa-list/", vazifa_l,name = 'vazifa-list'),
    
]
