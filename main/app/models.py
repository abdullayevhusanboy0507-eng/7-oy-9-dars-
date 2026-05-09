from django.db import models
from django.core.validators import MinValueValidator

class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    full_name = models.CharField(max_length=255)
    year = models.DateField()
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to="images/", blank=True , null=True)
    coursies = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name 