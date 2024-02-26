from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.http import Http404
from .models import Student , StudentSeralizers
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class StudentListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSeralizers
    
class StudentretriveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSeralizers
