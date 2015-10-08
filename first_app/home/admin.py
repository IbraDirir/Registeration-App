from django.contrib import admin
from .models import Student
from .forms import StudentForm
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    form = StudentForm


admin.site.register(Student, StudentAdmin)