from django.db import models

# Create your models here.
class Service(models.Model):
    serviceid = models.IntegerField(primary_key=True)
    servicenam = models.CharField(max_length=100)
    servicedes = models.CharField(max_length=100)
    serviceav = models.CharField(max_length=20)
    servicepr = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

class Bookings(models.Model):
    name = models.CharField(max_length=100)
    zip = models.CharField(max_length=5)
    service = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, default='')
    email = models.EmailField()
    message = models.TextField()