from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices
from django.db.models import Sum


class Package(models.Model):
    name = models.CharField(max_length=100, unique=False)
    info = models.TextField(max_length=200, blank=True, null=True)
    discount = models.PositiveSmallIntegerField(default=0)
    virtual_machines = models.ManyToManyField('VirtualMachine')
    datacenter = models.ForeignKey('Datacenter')
    features = models.ManyToManyField('Feature')
    STATUS = Choices('active', 'archive')
    status = StatusField(default='active')

    @property
    def total_price(self):
        price = self.features.all().aggregate(Sum('price'))['price__sum'] +\
                      self.virtual_machines.all().aggregate(Sum('price'))['price__sum']
        if self.discount > 0:
            price *= (100-self.discount) / 100
        return price

    def __str__(self):
        return self.name


class Datacenter(models.Model):
    location = models.CharField(max_length=100)
    available_machines = models.ManyToManyField('VirtualMachine')

    def __str__(self):
        return self.location


class Feature(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    info = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class VirtualMachine(models.Model):
    name = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
