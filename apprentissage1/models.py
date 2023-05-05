
from django.db import models
from django.contrib.auth.models import User    


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self) :
        return f"{self.first_name} {self.last_name}"
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self) :
        return f"{self.first_name} {self.last_name}"

    

class Course(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    hours = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)



class nomModel(models.Model):
    champ1 =models.CharField(max_length=45)
    champ2 =models.CharField(max_length=45)
    champ3 =models.BooleanField(default=True)
    champ4 =models.DateField()
    def __str__(self):
        return self.champ1
    class Meta:
        verbose_name ="Django Admin Tutorial"
        verbose_name_plural="Django Admin Tutorials"