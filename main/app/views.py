from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from .models import Course, Student
from .forms import CourseForm, StudentForm

def views_all(request: HttpRequest):
    coursies = Course.objects.all()
    students = Student.objects.all()
    
    context = {
        'coursies': coursies,
        'students': students,
    }
    
    return render(request, 'app/index.html', context)


def course_by(request, pk):
    coursies = get_object_or_404(Course, id=pk)
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


@login_required(login_url='home')
def add_course(request: HttpRequest):
    if request.user.is_staff:
        if request.method == 'POST':
            form = CourseForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                course = form.save()
                return redirect('coursies_by', pk=course.id)
        else:
            form = CourseForm()
        context = {
            'form':form
        }  
        return render(request,'app/add_course.html',context)
    else:
        return redirect('home')
    

@login_required(login_url='home')
def add_student(request: HttpRequest):
    if request.user.is_staff:
        if request.method == 'POST':
            form = StudentForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                student = form.save()
                return redirect('coursies_by',pk=student.coursies.id)
            
        else:
            form = StudentForm()
        context = {
            'form':form
        }
        return render(request, 'app/add_student.html', context)
    else:
        return redirect('home')