from django.contrib import admin
from django.urls import path, include
from. import views
urlpatterns = [
    path('',views.admin_page,name="admin_page"),
    path('hodentry',views.hodentry,name="hodentry"),
    path('hodprofile',views.hodprofile,name="hodprofile"),
    
    path('facultyentry',views.facultyentry,name="facultyentry"),
    path('facultyprofile',views.facultyprofile,name="facultyprofile"),
    

    path('studententry',views.studententry,name="studententry"),
    path('studentprofile',views.studentprofile,name="studentprofile"),
    
    path('adminentry',views.adminentry,name="adminentry"),
 
    path('adminsignout',views.adminsignout,name="adminsignout"),
]