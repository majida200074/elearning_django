from django.contrib import admin

from apprentissage1.models import Enrollment, Student, Teacher, Course

# Register your models here.


@admin.register(Student)
class adminStudent(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

@admin.register(Teacher)
class adminTeacher(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')




@admin.register(Enrollment)
class adminEnrollement(admin.ModelAdmin):
    list_display = ('student', 'course')               

@admin.register(Course)
class adminEnrollement(admin.ModelAdmin):
    list_display = ('name', 'description','teacher', 'start_date', 'end_date')


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Teacher
from .forms import TeacherCreationForm, TeacherChangeForm

class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'teachers'

from django.contrib.auth.models import User
class CustomUserAdmin(UserAdmin):
    add_form = TeacherCreationForm
    form = TeacherChangeForm
    model = Teacher
    inlines = (TeacherInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


   