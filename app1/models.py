from django.db import models

# Create your models here.
class Person(models.Model):
    length = models.IntegerField(default=0)
    uppercase = models.BooleanField(default=True)
    digits = models.BooleanField(default=True)
    special = models.BooleanField(default=True)
    def __str__(self):
        return str(self.length)