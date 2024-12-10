from django.db import models
from employee.models import Employee
from django.contrib.auth.models import User


# Create your models here.
class Leave(models.Model):
    title= models.CharField(max_length=50)
    details= models.TextField()
    dateRequested = models.DateTimeField(auto_now_add=True)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.BooleanField(False)
    approvedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title