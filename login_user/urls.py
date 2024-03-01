from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('',views.home,name="home"),
    path('hodsignin',views.hodsignin,name="hodsignin"),
    path('facultysignin',views.facultysignin,name="facultysignin"),
    path('studentsignin',views.studentsignin,name="studentsignin"),
    path('adminsignin',views.adminsignin,name="adminsignin"),
]