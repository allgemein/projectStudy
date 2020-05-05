from django.db import models

# Create your models here.
class status(models.Model):
    direction = models.CharField(default="front",max_length=100)
    power = models.IntegerField(default=0)
    def __str__(self):
        return str(self.direction+","+str(self.power))
