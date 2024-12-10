from django.db import models
from department.models import Department

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    details= models.TextField()
    jobTitle = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name