from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    return render (request, "python_quiz/home.html", {})

def admin_login(request):
    if request.method =="POST":
        admin_firstname = request.POST.get("firstname")
        admin_lastname = request.POST.get("lastname")
        admin_id = request.POST.get("student_id")
        email_id = request.POST.get("email_id")
        password = request.POST.get("password")
        reenter = request.POST.get("reenter")

     #Create model object and set data
        a= administrator_login()
        a.firstname =admin_firstname
        a.lastname = admin_lastname
        a.admin_id = admin_id
        a.admin_email_id =email_id
        a.admin_password = password
        a.reenter = reenter      

        #save data
        a.save()
        return redirect ("/python_quiz/home/")
    

