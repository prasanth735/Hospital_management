from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):

    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Doctors(models.Model):

    name=models.CharField(max_length=200)
    department_object=models.ForeignKey(Department,on_delete=models.CASCADE)
    duty_start=models.TimeField()
    duty_end=models.TimeField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)



class Appoinment(models.Model):

    name=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    doctor_object=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
