from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    createdBy = serializers.SerializerMethodField()

    def get_createdBy(self):
        request = self.context.get("request")
        return request.user.id

    class Meta:
        model = Employee
        fields = [ "name", "contact", "details", "jobTitle", "department", "createdBy" ]

    
    def create(self, validated_data):
        request = self.context.get("request")
        record = Employee.objects.create(createdBy = request.user, **validated_data)
        return record
