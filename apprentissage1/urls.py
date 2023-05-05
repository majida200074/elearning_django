

from django.urls import path
from . import views 
from .views import  index, admin_redirect
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    
    path('enrollment/add/', views.add_enrollment, name='add_enrollment'),
    path('enrollment/edit/<int:pk>/', views.edit_enrollment, name='edit_enrollment'),
    path('enrollment/delete/<int:enrollment_id>/', views.EnrollmentDeleteView.as_view(), name='EnrollmentDeleteView'),
    path('enrollment_list/', views.enrollment_list, name='enrollment_list'),    
    #path('course/delete/<int:course_id>/', views.delete_course, name='course_delete'),
    path('course/delete/<int:pk>/', views.delete_course, name='course_delete'),
    path('course/add/', views.ajouter_cours, name='course_create'),
    path('course_list/', views.course_list, name='course_list'),
    path('course/edit/<int:pk>/', views.edit_course, name='course_edit'),
    path('student/delete/<int:student_id>/', views.delete_student, name='student_delete'),
    path('student/add/', views.add_student, name='student_create'),
    path('student_list', views.student_list, name='student_list'),
    path('student/edit/<int:student_id>/', views.edit_student, name='student_edit'),
    path('teacher/delete/<int:id>/', views.supprimer_enseignant, name='teacher_delete'),
    path('teacher/add/', views.teacher_add, name='teacher_create'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('teacher/edit/<int:teacher_id>/', views.teacher_edit, name='teacher_edit'),
   #path('login/', user_login, name='login'),
    path('', views.index, name='index'),
    path('home/', index, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    path('get-course-info/', views.get_course_info, name='get-course-info'),
    
    path('admin/', admin_redirect, name='admin-button'),
   
  
   
]
