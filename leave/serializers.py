from rest_framework import serializers
from .models import Leave
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = [ "title", "details", "dateRequested", "employeeID", "status" ]
    
    def save(self):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = get_object_or_404(User, username=(request.data['username']))
            token = Token.objects.get_or_create(user=user)

            # User.objects.get(username = CurrentUserDefault())
            # approvedBy = CurrentUserDefault()
            print("Current User =============> :", token)

