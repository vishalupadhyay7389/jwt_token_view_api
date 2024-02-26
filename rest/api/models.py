from django.db import models
from rest_framework import serializers


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class StudentSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
