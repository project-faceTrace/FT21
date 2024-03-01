from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
import mysql.connector as sql
# Create your views here.
username=''
password=''
id=''
def home(request):
   # return HttpResponse("Hello I am working") 
    return render(request,"login_user/index.html")
def hodsignin(request):
    if request.method == "POST":
       
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="hod_id":
                id=value
            
            if key=='password':
                password=value
        # hodemail=request.POST['hod_email']
            
        c="select* from hod where hod_id = '{}'and password='{}'".format(id,password)
        
        cursor.execute(c)
       
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"login_user/error.html.html")    
        else:    
            return render(request,"hod_page/hod_page.html")
        
    return render(request,"login_user/hodsignin.html")

def facultysignin(request):
    if request.method == "POST":
        
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="faculty_id":
                id=value
            
            if key=='password':
                password=value
            
        c="select* from faculty where faculty_id = '{}' and password = '{}';".format(id,password)
        
        cursor.execute(c)
       
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"login_user/error.html")        
        else:
            render(request,"faculty_page/faculty_page.html")
            
    return render(request,"login_user/facultysignin.html")

def studentsignin(request):
    if request.method == "POST":
        
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="student_id":
                id=value
            
            if key=='password':
                password=value
            
        c="select* from student where student_id = '{}' and password = '{}';".format(id,password)
        
        cursor.execute(c)
       
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"login_user/error.html")    
        else:    
            return render(request,"student_page/student_page.html")
        
    return render(request,"login_user/studentsignin.html")

def adminsignin(request):
    if request.method == "POST":
        
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="admin_id":
                id=value
            
            if key=='password':
                password=value
            
        c="select* from admin where admin_id = '{}'and password = '{}' ".format(id,password)
        
        cursor.execute(c)
       
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"login_user/error.html")    
        else:    
            return render(request,"admin_page/admin_page.html")
        
    return render(request,"login_user/adminsignin.html")