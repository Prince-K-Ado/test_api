from django.db import models
 
# Create your models here.
 
class Employee(models.Model):
    Employeeid     = models.AutoField(primary_key=True)
    EmplyeeName    = models.CharField(max_length=255)
    EmployeeEmail  = models.CharField(max_length=255)
    PhotoFileName  = models.CharField(max_length=255)
    DepartmentName = models.CharField(max_length=255)
    DateOfJoining  = models.DateField()
    EmployeeSalary = models.FloatField()
 
class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=255)