from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from .models import Course, Student


def views_all(request: HttpRequest):
    coursies = Course.objects.all()
    students = Student.objects.all()
    
    context = {
        'coursies': coursies,
        'students': students,
    }
    
    return render(request, 'app/index.html', context)


def course_by(request, pk):
    coursies = Course.objects.filter(id=pk)
    students = Student.objects.filter(coursies=coursies)

    context = {
        "coursies": coursies,
        "students": students,
    }

    return render(request, "app/index.html", context)


def student_detail(request, pk):
    students = Student.objects.get(id=pk)
    
    context = {
        "student": students,
    }
    
    return render(request, "app/detail.html", context)