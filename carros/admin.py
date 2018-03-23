# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Carro, Fabricante
# Register your models here.

admin.site.register(Carro)
admin.site.register(Fabricante)
