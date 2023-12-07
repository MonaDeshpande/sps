from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import *
from .forms import administrator_login_form, administrator_signin_form
from .models import administrator_login,administrator_signin
# from django.views import View

# Create your views here.
def home(request):
    Administrator_login= administrator_login.objects.all()
    #will bring student in dictionary
    return render(request, "python_quiz/home.html", {
        'administrator_login': Administrator_login
    })
    return render (request, "python_quiz/home.html", {})


def admin_login(request):

    form = administrator_login_form()
  
    if request.method =="POST":
        form = administrator_login_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'python_quiz/admin_signup.html', context)
    

def admin_details(request):
    administrator_details = administrator_login.objects.all
    return render (request, "python_quiz/admin_details.html", {'administrator_details': administrator_details})

def delete_admin(request, admin_id):
    print(admin_id)
    x=administrator_login.objects.get(admin_id=admin_id)
    print(x)
    x.delete()
    return redirect("/python_quiz/home/")

def update_admin(request, admin_id):
    data = administrator_login.objects.get(admin_id=admin_id)
    form = administrator_login_form(instance=data)

    if request.method =="POST":
        form = administrator_login_form(request.POST, instance=data)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'python_quiz/admin_signup.html', context)

def sign_in(request):
    form = administrator_signin_form()
  
    if request.method =="POST":
        form = administrator_signin_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'python_quiz/admin_signin.html', context)

def add_questions(request, admin_id):
    form = administrator_signin_form()
    Administrator_Signin= administrator_signin.objects.get(admin_id = admin_id)
    email2 = Administrator_Signin.email_id
    password2 =Administrator_Signin.password

    form = administrator_login_form()
    Administrator_Login= administrator_login.objects.get(admin_id = admin_id)
    email1 = Administrator_Login.email_id
    password1 =Administrator_Login.password

    if email1 ==email2 and password1 == password2:
        return redirect("/python_quiz/questions/")
    else:
        return HttpResponse("Email id or password doesnt match")



    
