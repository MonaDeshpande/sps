from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import *
from .form import administrator_login_form
from .models import administrator_login
from django.views import View
from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, "python_quiz/home.html", {})

def admin_login(request):
    return render (request, "python_quiz/Admin_login.html", {})

# def add_administrator(request):
    print("received request")
    if request.method =="POST":
        admin_firstname = request.POST.get("firstname")
        admin_lastname = request.POST.get("lastname")
        admin_id = request.POST.get("student_id")
        image= request.POST.get("image")
        emailid =request.POST.get("email")
        password = request.POST.get("password")
        reenter = request.POST.get("reenter")

     #Create model object and set data
        a= administrator_login()
        a.firstname =admin_firstname
        a.lastname = admin_lastname
        a.admin_id = admin_id
        a.image = image
        a.email_id =emailid
        a.password = password
        a.reenter_password = reenter      

        #save data
        a.save()
        return redirect ("/python_quiz/home/")

class formView(View):
    def get(self, request):
        form =administrator_login_form()
        # print(form.as_p())
        return render(request, "python_quiz/Admin_login.html", {'form':form} )
    
 
# def form_view(request):
#     HttpResponse("Render request initiated")
#     context ={}
 
#     # create object of form
#     form = administrator_login(request.POST or None, request.FILES or None)
     
#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()
 
#     context['form']= form
#     return render(request, "python_quiz/Admin_login.html", context)


