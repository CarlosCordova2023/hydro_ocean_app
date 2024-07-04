from django.db import models

# Create your models here.

class Observation(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    salinity = models.FloatField()

    def __str__(self):
        return f"{self.location} on {self.date}"
