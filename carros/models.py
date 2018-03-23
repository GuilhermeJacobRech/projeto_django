# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nome = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    name = models.CharField(max_length=300,null=True)
    valor = models.DecimalField(decimal_places=0,max_digits=100,null=True)
    ano = models.IntegerField(null=True)
    modelo = models.CharField(max_length=200,null=True)
    fabricante = models.ForeignKey(Fabricante, null=True)


    def __str__(self):
        return self.name
