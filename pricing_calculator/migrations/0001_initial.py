# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datacenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('info', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True, max_length=200, null=True)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
                ('status', model_utils.fields.StatusField(choices=[('active', 'active'), ('archive', 'archive')], default='active', max_length=100, no_check_for_status=True)),
                ('datacenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricing_calculator.Datacenter')),
                ('features', models.ManyToManyField(to='pricing_calculator.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='VirtualMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('cpu', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('storage', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='virtual_machines',
            field=models.ManyToManyField(to='pricing_calculator.VirtualMachine'),
        ),
        migrations.AddField(
            model_name='datacenter',
            name='available_machines',
            field=models.ManyToManyField(to='pricing_calculator.VirtualMachine'),
        ),
    ]
