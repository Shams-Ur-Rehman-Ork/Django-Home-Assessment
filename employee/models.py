from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    hire_date = models.DateField()

    def __str__(self):
        return self.name


