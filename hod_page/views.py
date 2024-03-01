from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages
import mysql.connector as sql
# Create your views here.
username=''
password=''
id=''


def hod_page(request):
   # return HttpResponse("Hello I am working") 
    return render(request,"hod_page/hod_page.html")
# Create your views here.

def hodsignout(request):
    pass