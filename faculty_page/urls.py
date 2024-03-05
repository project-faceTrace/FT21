from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('',views.faculty_page,name="faculty_page"), 
    path('facultysignout',views.facultysignout,name="facultysignout"),
]