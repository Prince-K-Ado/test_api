# Generated by Django 5.0.1 on 2024-01-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employeeid', models.AutoField(primary_key=True, serialize=False)),
                ('EmplyeeName', models.CharField(max_length=255)),
                ('EmployeeEmail', models.CharField(max_length=255)),
                ('PhotoFileName', models.CharField(max_length=255)),
                ('DepartmentName', models.CharField(max_length=255)),
                ('DateOfJoining', models.DateField()),
                ('EmployeeSalary', models.FloatField()),
            ],
        ),
    ]
