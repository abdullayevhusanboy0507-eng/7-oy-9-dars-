from django.urls import path

from .views import views_all, course_by, student_detail

urlpatterns = [
    path('',views_all, name='home'),
    path('coursies/<int:pk>', course_by, name='coursies_by'),
    path('syudent_detail/<int:pk>/', student_detail, name='student_detail'),
    
]