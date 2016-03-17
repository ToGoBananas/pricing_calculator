from django.db import models
from django.db.models import Sum

from model_utils.models import TimeStampedModel
from pricing_calculator.models import Package, Datacenter, Feature


class Order(TimeStampedModel):
    email = models.EmailField()
    packages = models.ManyToManyField(Package)

    @property
    def total_price(self):
        return self.packages.aggregate(Sum('total_price'))['total_price__sum']

    def __str__(self):
        return self.email

    class Meta:
        abstract = False
