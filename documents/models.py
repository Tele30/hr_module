from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    POSITION = (
        ("employee", "Employee"),
        ("hr", "Human Resource"),
        ("manager", "Manager"),
    )
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=50, choices=POSITION)



class Contract(models.Model):
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class HolidayRequest(models.Model):
    STATUS = (
        ("pending", "Pending"),
        ("rejected", "Rejected"),
        ("accepted", "Accepted"),
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=25, choices=STATUS)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee")
    replacement = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="replacement")


class CertificateEmployee(models.Model):
    date = models.DateField()
    reason = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
