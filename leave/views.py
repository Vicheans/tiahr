from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Leave
from .serializers import LeaveSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LeaveListCreate(generics.ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class LeaveRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    lookup_field = "pk"