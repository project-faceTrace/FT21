from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
import mysql.connector as sql
# Create your views here.
username=''
password=''
id=''


def hod_page(request):
    if request.user.is_authenticated:
        return render(request,"hod_page/hod_page.html")
    else:
        return redirect('login_user/index.html')
# Create your views here.

def hodsignout(request):
    logout(request)
    return redirect('home')
