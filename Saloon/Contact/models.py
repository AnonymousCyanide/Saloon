from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length = 60)
    phone = models.CharField(max_length=12)
    message = models.CharField(max_length= 400)
    date = models.DateTimeField( auto_now_add=True)

    def __str__(self) -> str:
        return self.email + ' - ' + str(self.date)

