from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer

# Create your views here.
class DepartmentListCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = "pk"