from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
import mysql.connector as sql
# Create your views here.



def faculty_page(request):   
    return render(request,"faculty_page/faculty_page.html")


def facultysignout(request):
    pass
