from django.shortcuts import render
from django.http import HttpResponse
from invitation.models import Student
from django.template import loader
from django.shortcuts import get_object_or_404
import json

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def request(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    first_name = body['firstName']
    last_name = body['lastName']
    email = body['email']
    entrance = body['entrance']
    department = "CMPE"
    student = Student(name= first_name + " " + last_name, email=email, entrance=entrance, department=department)
    student.save()
    return HttpResponse(student)

def invite(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return HttpResponse(student)
