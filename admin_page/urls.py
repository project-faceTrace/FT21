from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('',views.admin_page,name="admin_page"),
     path('hodentry',views.hodentry,name="hodentry"),
    
    
     path('facultyentry',views.facultyentry,name="facultyentry"),
    

     path('studententry',views.studententry,name="studententry"),
    
    
     path('adminentry',views.adminentry,name="adminentry"),
 
    path('adminsignout',views.adminsignout,name="adminsignout"),
]