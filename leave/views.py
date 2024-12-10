from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Leave
from .serializers import LeaveSerializer

# Create your views here.
class LeaveListCreate(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer



class LeaveRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    lookup_field = "pk"