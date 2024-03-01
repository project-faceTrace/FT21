from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages
import mysql.connector as sql
# Create your views here.
def student_page(request):
   
    return render(request,"student_page/student_page.html")

def studentsignout(request):
    pass