from django import forms

from .models import Course, Student


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'name': 'Nomi',
            'price': 'Narxi',
        }
        
    
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'full_name': 'Toliq ismi',
            'year': 'yili',
            'phone_number': 'telefon raqam',
            'image': 'rasmi',
            'coursies': 'kursi',
        }