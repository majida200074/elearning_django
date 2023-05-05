from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, TeacherForm, CourseForm, EnrollmentForm,LoginForm
from .models import Student, Teacher, Course, Enrollment
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Course
import requests
from .models import *
from bs4 import BeautifulSoup



import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Course

def get_course_info(request):
    # Extraire les informations sur les cours à partir de la page d'accueil d'Udacity avec BeautifulSoup
    url = "https://www.coursera.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    courses = []
    for course in soup.find_all('div', {'class': 'offering-wrapper'}):
        name = course.find('h2', {'class': 'color-primary-text headline-1-text'}).text.strip()
        desc = course.find('div', {'class': 'offering-description'}).text.strip()
        courses.append({'name': name, 'description': desc})
        Course.objects.create(name=name, description=desc)

    # Paginer les cours extraits
    paginator = Paginator(courses, 10) # Afficher 10 cours par page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Afficher les cours extraits dans une page HTML de pagination
    return render(request, 'course_list.html', {'page_obj': page_obj})









@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    paginator =Paginator(students, 5)
    page = request.GET.get('page', 1)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    return render(request, '../templates/student_list.html', {'students': students, 'paginator':paginator})
# Create your views here.



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, '../templates/student_add.html', {'form': form})





def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, '../templates/edit_student.html', {'form': form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, '../templates/delete_student.html', {'student': student})

@login_required(login_url='login')
def teacher_list(request):
    teachers = Teacher.objects.all()
    paginator =Paginator(teachers, 5)
    page = request.GET.get('page', 1)
    try:
        teachers = paginator.page(page)
    except PageNotAnInteger:
        teachers = paginator.page(1)
    except EmptyPage:
        teachers = paginator.page(paginator.num_pages)
    return render(request, '../templates/teacher_list.html', {'teachers': teachers, 'paginator':paginator})



def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, '../templates/ajouterenseignant.html', {'form': form})



def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, '../templates/edit_teacher.html', {'form': form})


def supprimer_enseignant(request, id):
    enseignant = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('teacher_list')

    return render(request, '../templates/delete_teacher.html', {'enseignant': enseignant})


@login_required(login_url='login')

def course_list(request):
    courses = Course.objects.all()
    paginator =Paginator(courses, 5)
    page = request.GET.get('page', 1)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)       
    return render(request, '../templates/course_list.html', {'courses': courses, 'paginator':paginator})

# views.py


def ajouter_cours(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, '../templates/add_course.html', {'form': form})


def edit_course(request, pk):
    # Récupération du cours à éditer
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        # Traitement des données du formulaire en POST
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            # Enregistrement des modifications et redirection vers la liste des cours
            form.save()
            return redirect('course_list')
    else:
        # Affichage du formulaire avec les données du cours à éditer
        form = CourseForm(instance=course)
    return render(request, '../templates/edit_course.html', {'form': form, 'course':course})




def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})





@login_required(login_url='login')

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    paginator =Paginator(enrollments, 5)
    page = request.GET.get('page', 1)
    try:
        enrollments = paginator.page(page)
    except PageNotAnInteger:
        enrollments = paginator.page(1)
    except EmptyPage:
        enrollments = paginator.page(paginator.num_pages)
    return render(request, '../templates/enrollment_list.html', {'enrollments': enrollments, 'paginator':paginator})



def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
        return render(request, '../templates/add_enrollment.html', {'form': form})


def edit_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, '../templates/edit_enrollment.html', {'form': form})


class EnrollmentDeleteView(View):
    def get(self, request, enrollment_id):
        enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
        return render(request, '../templates/delete_enrollment.html', {'enrollment': enrollment})

    def post(self, request, enrollment_id):
        enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
        enrollment.delete()
        return redirect('enrollment_list')
    

def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("L'authentification a été effectué avec succès" )
                else: 
                    return HttpResponse ("Le compte est désactivée")
            else:
                return HttpResponse ("Identifiant non valide")
    else:
        form = LoginForm()
        return render(request, '../templates/login.html',{'form': form} )

def admin_redirect(request):
    url = reverse('admin:index')
    return redirect(url)   

def index(request):
    base_url = 'https://www.datacamp.com/search'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/58.0.3029.110 Safari/537.3'}

    # Make a GET request to the base URL and get the HTML content
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all course cards on the page
    course_cards = soup.find_all('article',attrs= {'class': 'dc-card dc-card--bordered dc-card--interactive dc-global-search-result'})
    for card in course_cards:
        title = card.find('h4', attrs={}).text
        description = card.find('p', attrs={'class':'dc-u-mv-8'}).text
        link = card.find('a', attrs={'class':'shim ds-snowplow-search-v2-result-course'})
        hours = card.find('span', attrs={"class": None}).text 
        if not Course.objects.filter(title=title):
            if link is not None :
                c = Course(title=title, description=description, link=link['href'], hours=hours)  
                c.save()
    courses = Course.objects.all()
    paginator = Paginator(courses, 12) # Afficher 10 cours par page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    contexte = {
        'courses': courses,
        'page_obj':page_obj,
    } 
    return render(request, '../templates/index.html', contexte)

 