from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('',views.student_page,name="student_page"),
    path('studentsignout',views.studentsignout,name="studentsignout"),
]