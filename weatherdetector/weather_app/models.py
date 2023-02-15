from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=20)
    # country_code = models.IntegerField()
    # coordinate = models.CharField(max_length=20)
    # temperature = models.DecimalField()
    # pressure = models.DecimalField()
    # humidity = models.DecimalField()
