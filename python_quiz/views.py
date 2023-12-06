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
    return render (request, "python_quiz/home.html", {})


def admin_login(request):
    form = administrator_login_form()

    if request.method =="POST":
        form = administrator_login_form(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'python_quiz/Admin_login.html', context)

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
    context = {'form': form}
    return render(request, 'python_quiz/Admin_login.html', context)





