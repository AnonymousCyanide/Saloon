from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(User):
    class Meta :
        verbose_name = "Employee"
    rating = models.FloatField()
    time_slot = models.JSONField(default= '')

    def __str__(self) -> str:
        return self.username + '-' + 'Employee'

class Customer(User):
    class Meta :
        verbose_name = "Customer"
    

    def __str__(self) -> str:
        return self.username + '-' + 'Customer'

class Appointment(models.Model):
    class Meta:
        unique_together = ('employee','date','time_slot')
    TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )
    employee = models.ForeignKey('Employee',on_delete = models.CASCADE)
    date = models.DateField(help_text="YYYY-MM-DD")
    time_slot = models.IntegerField(choices=TIMESLOT_LIST)
    customer = models.ForeignKey('Customer',on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.employee.username + '-' + str(self.time_slot)

    def time(self):
        return self.TIMESLOT_LIST[self.time_slot][1]

