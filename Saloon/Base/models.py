from django.db import models
#from django.contrib.auth import User
# Create your models here.

class Featured(models.Model):
    image = models.ImageField(upload_to = 'static/uploads')
    heading = models.CharField(max_length=40 , default='THE BEACON TO ALL MANKIND')
    quote = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.heading
    
    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = Featured.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except Featured.DoesNotExist:
                pass
        super(Featured, self).save(*args, **kwargs)

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,default='The Father')
    image = models.ImageField(upload_to = 'static/uploads')
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name + '-' + str(self.id)