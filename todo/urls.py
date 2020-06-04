from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name="home"),
    path('main' , views.todo_tasks , name="main"),
]