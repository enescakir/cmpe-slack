from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'entrance', 'invite_button')
    list_filter = ['inviter']
    search_fields = ['name','email', 'entrance']
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/invite.js',   # app static folder
        )

admin.site.register(Student, StudentAdmin)
