from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    station = models.CharField(max_length=50)
    door = models.IntegerField(default=-1)
    time = models.TimeField(auto_now=False,auto_now_add=True)    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    car = models.IntegerField(default=-1)
    def __str__(self):
        return self.station
