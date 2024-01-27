# convert complex data models into native python datatypes
 
from rest_framework import serializers
from TestApp.models import Employee, Department
 
 
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
 
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"