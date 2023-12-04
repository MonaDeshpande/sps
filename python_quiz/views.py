from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import *
from .forms import administrator_login_form
from .models import administrator_login
# from django.views import View

# Create your views here.
def home(request):
    Administrator_login= administrator_login.objects.all()
    #will bring student in dictionary
    return render(request, "python_quiz/home.html", {
        'administrator_login': Administrator_login
    })
    #return render (request, "python_quiz/home.html", {})

# def admin_login(request):
#     return render (request, "python_quiz/Admin_login.html", {})

# add_administrator(request):
#     print("received request")
#     if request.method =="POST":
#         admin_firstname = request.POST.get("firstname")
#         admin_lastname = request.POST.get("lastname")
#         admin_id = request.POST.get("student_id")
#         image= request.POST.get("image")
#         emailid =request.POST.get("email")
#         password = request.POST.get("password")
#         reenter = request.POST.get("reenter")

#      #Create model object and set data
#         a= administrator_login()
#         a.firstname =admin_firstname
#         a.lastname = admin_lastname
#         a.admin_id = admin_id
#         a.image = image
#         a.email_id =emailid
#         a.password = password
#         a.reenter_password = reenter      

#         #save data
#         a.save()
#         return redirect ("/python_quiz/home/")

def admin_login(request):
    # def get(self, request):
     form =administrator_login_form()
     return render(request, "python_quiz/Admin_login.html", {'form':form} )
def save (self, request):
    if request.method == "POST":
        form = administrator_login_form(request.POST) 
        if form.is_valid():
            form.save
            print("data saved")
        else:
            return render(request, "python_quiz/Admin_login.html", {'form':form} )
    else:
        form = administrator_login_form(request.POST)
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


