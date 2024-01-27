from django.urls import path
from .views import  employeeApi, departmentApi, SaveFile, home_Testapp_view
# from django.conf.urls import re_path
# from TestApp import views
 
 
urlpatterns = [
     # Home page URL
    path('', home_Testapp_view, name='home'), # Forwarding the home page from project level urls.py to app level urls.py
    # url(r'^employee$', views.employeeApi), # Forwarding the employee page from project level urls.py to app level urls.py
    # url(r'^employee/([0-9]+)$', views.employeeApi),
 
     # URL for listing all employees or adding a new employee (GET, POST)
    path('employee/', employeeApi, name='employee-list'),
 
    # URL for getting, updating, or deleting a specific employee (GET, PUT, DELETE)
    path('employee/<int:id>/', employeeApi, name='employee-detail'),
    
 
    # URL for listing all departments or adding a new department (GET, POST)
    path('department/', departmentApi, name='department-list'),
    path('department/<int:id>/', departmentApi, name='department-detail'),
 
    # File upload URL
    path('employee/SaveFile', SaveFile, name='save-file'),
    
]