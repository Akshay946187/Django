from django.db import models

# Create your models here.


class Emp(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=120)
    addres = models.CharField(max_length=100)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=100)