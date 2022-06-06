from django.contrib import admin
from django.urls import path, include
from .views import view_name
urlpatterns = [
    path('', view_name, name="view_name"),
]