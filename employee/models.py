from django.db import models
from django.utils.timezone import now

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.employee_name
