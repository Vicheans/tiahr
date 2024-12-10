from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee

# Create your models here.
class Attendance(models.Model):
    clockIn= models.DateTimeField()
    clockOut = models.DateTimeField()
    employeeID = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.employeeID