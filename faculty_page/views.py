from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
import mysql.connector as sql
# Create your views here.



def faculty_page(request):   
    if request.user.is_authenticated:
        return render(request,"faculty_page/faculty_page.html")
    else:
        return redirect(request,'login_user/index.html')



def facultysignout(request):
    logout(request)
    return redirect('home')
