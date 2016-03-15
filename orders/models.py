from django.db import models

from model_utils.models import TimeStampedModel
from pricing_calculator.models import Package, Datacenter, Feature


class Order(TimeStampedModel):
    email = models.EmailField()
    package = models.ForeignKey(Package)
    datacenters = models.ManyToManyField(Datacenter)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.email
