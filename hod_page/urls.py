from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('',views.hod_page,name="hod_page"), 
    path('hodsignout',views.hodsignout,name="hodsignout"),
]