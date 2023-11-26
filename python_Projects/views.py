from django.shortcuts import render
# from django.urls import HttpResponse


# Create your views here.
def guess_number_user(request):
    return render (request, "/guess_number_user.py", {})

