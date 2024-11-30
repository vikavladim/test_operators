from django.db import models

class Operator(models.Model):
    ne = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    gsm = models.BooleanField(null=True, blank=True)
    umts = models.BooleanField(null=True, blank=True)
    lte = models.BooleanField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
