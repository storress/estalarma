from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Auto(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=8)
    owner = models.CharField(max_length=50)
    class_name = models.CharField(max_length=30)

#    def __str__(self):
#        return self.plate
