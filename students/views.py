from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Students

def students_home(request):
    students = Students.objects.all()
    #will bring student in dictionary
    return render(request, "students/home.html", {
        'students':students
    })

def students_data(request):
    return render (request, "students/students_data.html", {})

def add_students(request):
     if request.method =="POST":
        #print("data is coming")
        #fetch data
        student_firstname = request.POST.get("firstname")
        student_lastname = request.POST.get("lastname")
        student_id = request.POST.get("student_id")
        print(student_id)

        #Create model object and set data
        s=Students()
        s.firstname =student_firstname
        s.lastname = student_lastname
        s.student_id = student_id

        #save data
        s.save()
        
     print("data is not coming")
     return render(request, "students/students_data.html", {})

def delete_student(request, student_id):
    print(student_id)
    x=Students.objects.get(pk=student_id)
    print(x)
    x.delete()
    return HttpResponse("Student removed successfully")

def update_student(request, student_id):
    student = Students.objects.get(pk=student_id)
    return render(request, "students/update.html", {
        'students':student
    })
    
def do_update(request,student_id):
    if request.method =="POST":
        #print("data is coming")
        #fetch data
        student_firstname = request.POST.get("firstname")
        student_lastname = request.POST.get("lastname")
        student_id_temp = request.POST.get("student_id")
        print(student_id)

        s = Students.objects.get(pk=student_id)

        #Create model object and set data
        s.firstname =student_firstname
        s.lastname = student_lastname
        s.student_id = student_id_temp

        #save data
        s.save()
    return HttpResponse("Updated Succesfuly")
    


