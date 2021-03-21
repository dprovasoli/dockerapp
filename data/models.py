from django.db import models
from django.conf import settings


# Create your models here.
class CsvData(models.Model):
    
    country = models.CharField(max_length=100, primary_key=True)
   
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
   
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.country

    class Meta:
        ordering = ['country']
