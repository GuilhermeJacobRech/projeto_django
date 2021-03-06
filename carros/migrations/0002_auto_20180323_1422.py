# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='ano',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='carro',
            name='modelo',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='carro',
            name='valor',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=100),
        ),
    ]
