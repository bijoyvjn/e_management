from django.db import models

# Create your models here.

class Department(models.Model):
    dep_no = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employe(models.Model):
    emp_no = models.CharField(max_length=50,unique=True)
    designation = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.emp_no