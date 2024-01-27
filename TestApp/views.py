from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
 
from TestApp.models import Employee, Department
from TestApp.serializers import EmployeeSerializer, DepartmentSerializer
from django.core.files.storage import default_storage
 
 
# Employee API
# Create Views here
@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)
 
# Department API
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        department = Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
 
 
# File Save API
@csrf_exempt
def SaveFile(request):
    if request.method == 'POST':
        file = request.FILES.get['uploadedFile', None]
        if file:
            file_name = default_storage.save(file.name, file)
            return JsonResponse({'message': 'File uploaded successfully', 'filen_name': file_name}, safe=False)
        else:
            return JsonResponse({'message' : 'No File Provided'}, status=400, safe=False)
    else:
        return JsonResponse({"message" : "Invalid request method"}, status=405, safe=False)
 
    # file = request.FILES['uploadedFile']
    # file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
 
def home_Testapp_view(request):
    return HttpResponse("Hello This has been a struggle!!!")
 
# Create your views here.