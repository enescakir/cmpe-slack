from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
import json
import requests
import os

from invitation.models import Student

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

@csrf_exempt
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
    
@csrf_exempt
def invite(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    data = {'email': student.email, 'token': os.environ.get('SLACK_ACCESS_TOKEN'), 'set_active': 'true'}
    url = 'https://' + os.environ.get('SLACK_TEAM_NAME') + '.slack.com/api/users.admin.invite'
    r = requests.post(url, data = data)
    return HttpResponse(r)
