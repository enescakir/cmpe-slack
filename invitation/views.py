from django.shortcuts import render
from django.http import HttpResponse
from invitation.models import Student

# Create your views here.


def index(request):
    return HttpResponse("Vue.js Index")

def request(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    entrance=request.POST['entrance']
    department="CMPE"

    student = Student(name= first_name + " " + last_name, email=email, entrance=entrance, deparment=deparment)
    student.save()
    return HttpResponse(student)
