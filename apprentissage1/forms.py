from django import forms
from .models import Student, Teacher, Course, Enrollment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Teacher



class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']





class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email']



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'



class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    fields = ['username', 'password']



class TeacherCreationForm(UserCreationForm):

    class Meta:
        model = Teacher
        fields = ('user','first_name','last_name','email') 
class TeacherChangeForm(UserChangeForm):

    class Meta:
        model = Teacher
        fields = ('user', 'first_name','last_name','email') 
