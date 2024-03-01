from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from admin_page.forms import ImageForm
import mysql.connector as sql
# Create your views here.
username=''
password=''
id=''
student_image=''
email=''
student_branch=''
def admin_page(request):
   # return HttpResponse("Hello I am working") 
    return render(request,"admin_page/admin_page.html")

def hodentry(request):
    if request.method == "POST":
       
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="hod_id":
                id=value
           
            if key=='password':
                password=value
            if key=="hod_name":
                name=value
            if key=="hod_email":
                email=value
            if key=="hod_contact":
                contact=value
        
        c="insert into hod(hod_id, hod_name, hod_email, hod_contact,password) values('{}','{}','{}','{}','{}')".format(id,name,email,contact,password)
        
        cursor.execute(c)
        
        conn.commit()
           
    
        return redirect('admin_page')
        

    return render(request,"admin_page/hodentry.html")


def facultyentry(request):
    if request.method == "POST":
     
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="faculty_id":
                id=value
            
            
            if key=='password':
                password=value
            if key=="faculty_name":
                name=value
            if key=="faculty_email":
                email=value
            if key=="faculty_contact":
                contact=value
       
        c="insert into faculty(faculty_id, faculty_name, faculty_email, faculty_contact,password) values('{}','{}','{}','{}','{}')".format(id,name,email,contact,password)
        
        cursor.execute(c)
        conn.commit()
        return redirect('admin_page')
    return render(request,"admin_page/facultyentry.html")

def studententry(request):
    
    if request.method == "POST":
        form=ImageForm(request.POST,request.FILES)
        if()
        context={'form':ImageForm()}
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="student_id":
               id=value
            
            if key=='password':
                password=value
            if key=="student_name":
                name=value
            if key=="student_email":
                email=value
            if key=="student_contact":
                contact=value
            if key=="student_branch":
                student_branch=value
            if key=="student_image":
                student_image=value
        
        c="insert into student(student_id, student_name, student_email, student_contact,branch,image,password) values('{}','{}','{}','{}','{}','{}','{}')".format(id,name,email,contact,student_branch,student_image,password)
        cursor.execute(c)
        conn.commit()
        return redirect('admin_page')
   

    return render(request,"admin_page/studententry.html")


def adminentry(request):
    if request.method == "POST":
    
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="admin_id":
               id=value
            
            if key=='password':
                password=value
            if key=="admin_name":
                name=value
            if key=="admin_email":
                email=value
            if key=="admin_contact":
                contact=value
        
        c="insert into admin(admin_id, admin_name, admin_email, admin_contact,password) values('{}','{}','{}','{}','{}')".format(id,name,email,contact,password)
        cursor.execute(c)
        conn.commit()
        return redirect('admin_page')
    return render(request,"admin_page/adminentry.html")


def adminsignout(request):
    pass