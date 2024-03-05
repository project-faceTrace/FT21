from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

import mysql.connector as sql
# Create your views here.
username=''
password=''
id=''

email=''
student_branch=''
def admin_page(request):
   # return HttpResponse("Hello I am working") 
    if request.user.is_authenticated:
        return render(request,"admin_page/admin_page.html")
    else:
        return redirect('home')

def hodentry(request):
    if request.method == "POST":
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        username=request.POST['hod_id']#session
        password=request.POST['password']#session
        cnfmpassword=request.POST['cnfm_password']#session
        if password==cnfmpassword:#session
            user=User.objects.create_user(username=username,password=password)#session
            user.save()#session
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
            # login(request,user)
            return redirect('admin_page')
        else:
            return redirect('admin_page/hodentry')
        
        
    return render(request,"admin_page/hodentry.html")
def hodprofile(request):
    return render(request,"hod_page/hodprofile.html")

def facultyentry(request):
    if request.method == "POST":
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        username=request.POST['faculty_id']#session
        password=request.POST['password']#session
        cnfmpassword=request.POST['cnfm_password']
        if password==cnfmpassword:#session
            user=User.objects.create_user(username=username,password=password)#session
            user.save()#session
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
            # login(request,user)
            return redirect(request,'admin_page/admin_page.html')
        else:
            return redirect(request,'admin_page/facultyentry.html')
        
        
    return render(request,"admin_page/adminentry.html")
def facultyprofile(request):
    return render(request,"faculty_page/facultyprofile.html")
def converttoBinary(filename):
    with open(filename,'rb') as file:
        binarydata=file.read()
    return binarydata
def convertBinarytoFile(binarydata,filename):
    with open(filename,'wb') as file:
        file.write(binarydata)


def studententry(request):
    
    if request.method == "POST":
        conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
        cursor=conn.cursor()
        d=request.POST
        username=request.POST['admin_id']#session
        password=request.POST['password']#session
        cnfmpassword=request.POST['cnfm_password']#session
        if password==cnfmpassword:#session
            user=User.objects.create_user(username=username,password=password)#session
            user.save()#session
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
            # convertPic=converttoBinary(student_image)
            c="insert into student(student_id, student_name, student_email, student_contact, branch, image, password) values( '{}','{}','{}','{}','{}','{}','{}' );".format(id,name,email,contact,student_branch,student_image,password)
            cursor.execute(c)
            conn.commit()
            return redirect(request,'admin_page/admin_page.html')
   

    return render(request,"admin_page/studententry.html")

def studentprofile(request):
    return render(request,"student_page/studentprofile.html")

def adminentry(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)#session
        if form.is_valid():#session
            user=form.save()#session
            conn=sql.connect(host="localhost",user="root",passwd="Jaishree@05",database='FT')
            cursor=conn.cursor()
            d=request.POST
            username=request.POST['admin_id']#session
            password=request.POST['password']#session
            cnfmpassword=request.POST['cnfm_password']#session
            if password==cnfmpassword:#session
                user=User.objects.create_user(username=username,password=password)#session
                user.save()#session
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
                login(request,user)#session
                return 'success'
                return redirect(request,'admin_page/admin_page.html')
            else:
                form=UserCreationForm()#session
                return redirect(request,'admin_page/adminentry.html',{'form':form})
        
        
    return render(request,"admin_page/adminentry.html")


def adminsignout(request):
    logout(request)#session
    return redirect('home')