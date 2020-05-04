from django.db import models

# Create your models here.
class status(models.Model):
    place = models.IntegerField(default=0)
    def __str__(self):
        return str(self.place)
