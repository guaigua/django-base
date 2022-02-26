from django.db import models

# Create your models here.


class Client(models.Model):

    # Address Fields
    address = models.TextField(max_length=250, null=True, blank=False)  # -- Si requered
    city = models.CharField('city', max_length=30, null=True, blank=False)  # -- Si requered
    state = models.CharField('state', max_length=30, null=True, blank=False)  # -- Si requered
    zip_code = models.CharField('zip', max_length=30, null=True, blank=False)  # -- Si requered
    country = models.CharField('country', max_length=30, null=True, blank=False)  # -- Si requered

    county = models.CharField('county', max_length=30, null=True, blank=True)  # -- Si requered
    route = models.CharField('route', max_length=30, null=True, blank=True)  # -- Si requered
    street_number = models.CharField('street number', max_length=30, null=True, blank=True)  # -- Si requered
    neighborhood = models.CharField('neighborhood', max_length=30, null=True, blank=True)  # -- Si requered
    latitude = models.DecimalField('latitude', max_digits=30, decimal_places=20, null=True, blank=True)  # -- Si requered
    longitude = models.DecimalField('longitude', max_digits=30, decimal_places=20, null=True, blank=True)  # -- Si requered