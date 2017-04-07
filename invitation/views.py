from django.shortcuts import render
from django.http import HttpResponse
from invitation.models import Student
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def request(request):
    first_name=request.POST['firstName']
    last_name=request.POST['lastName']
    email=request.POST['email']
    entrance=request.POST['entrance']
    department="CMPE"
    student = Student(name= first_name + " " + last_name, email=email, entrance=entrance, deparment=deparment)
    student.save()
    return HttpResponse(student)

def invite(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return HttpResponse(student)
