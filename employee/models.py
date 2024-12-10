from django.db import models
from department.models import Department
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    details= models.TextField()
    jobTitle = models.TextField()
    password = models.CharField(max_length=50, default=1111)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name