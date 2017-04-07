from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    entrance = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    inviter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def invite_button(self):
        if self.inviter:
            return self.inviter
        else:
            return mark_safe('<button id=' + str(self.id) + ' type="">Onayla</button>')

    def __str__(self):
        return self.name
