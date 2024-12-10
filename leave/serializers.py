from rest_framework import serializers
from .models import Leave
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

class LeaveSerializer(serializers.ModelSerializer):
    approvedBy = serializers.SerializerMethodField()

    def get_approvedBy(self):
        request = self.context.get("request")
        return request.user.id

    class Meta:
        model = Leave
        fields = [ "title", "details", "dateRequested", "employeeID", "status", "approvedBy" ]
    
    def create(self, validated_data):
        request = self.context.get("request")
        record = Leave.objects.create(approvedBy = request.user, **validated_data)
        return record

