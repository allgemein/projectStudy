from django.db import models

# Create your models here.
class delaytime(models.Model):
    delaysec = models.IntegerField(default=0)
    def __str__(self):
        return str(self.delaysec)+"ms"
