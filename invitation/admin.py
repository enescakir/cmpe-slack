from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'entrance', 'invite_button')
    list_filter = ['inviter']
    search_fields = ['name','email', 'entrance']

admin.site.register(Student, StudentAdmin)
