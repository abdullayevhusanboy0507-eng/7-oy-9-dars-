from django.urls import path

from .views import views_all, course_by, student_detail, add_course, add_student, update_student

urlpatterns = [
    path('',views_all, name='home'),
    path('coursies/<int:pk>', course_by, name='coursies_by'),
    path('update_student/<int:pk>', update_student, name='update_student'),
    path('student_detail/<int:pk>/', student_detail, name='student_detail'),
    path('course/create/',add_course, name='add_course'),
    path('student/create/',add_student, name='add_student'),
]