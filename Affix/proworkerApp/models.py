from django.db import models

class ProWorkers(models.Model):
    ProWorkerId = models.AutoField(primary_key=True)
    ProWorkerName = models.CharField(max_length=200)
    UrbanCity = models.CharField(max_length=100)
    JoinDate = models.DateField()
    ImageName = models.CharField(max_length=500)