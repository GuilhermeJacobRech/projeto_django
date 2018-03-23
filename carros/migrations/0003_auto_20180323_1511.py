# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 18:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0002_auto_20180323_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='carro',
            name='ano',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='modelo',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='valor',
            field=models.DecimalField(decimal_places=0, max_digits=100, null=True),
        ),
        migrations.AddField(
            model_name='carro',
            name='fabricante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carros.Fabricante'),
        ),
    ]