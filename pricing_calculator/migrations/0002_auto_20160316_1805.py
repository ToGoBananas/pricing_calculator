# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='features',
            field=models.ManyToManyField(blank=True, to='pricing_calculator.Feature'),
        ),
    ]
