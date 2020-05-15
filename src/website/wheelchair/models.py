from django.db import models

# Create your models here.

class Task(models.Model):
    station = models.CharField(max_length=50)
    door = models.IntegerField(default=-1)
    time = models.TimeField(auto_now=False,auto_now_add=True)    
    user = models.CharField(max_length=50)
    def __str__(self):
        return self.station
