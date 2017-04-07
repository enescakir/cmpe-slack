from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    entrance = models.CharField(max_length=4)
    created_at = models.DateTimeField()
    inviter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
