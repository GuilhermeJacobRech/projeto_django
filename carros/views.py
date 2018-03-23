# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Carro

# Create your views here.

def index(request):
    todos_carros = Carro.objects.all()

    template = loader.get_template('carros/index.html')
    return HttpResponse(template.render({
        'carros': todos_carros
    }, request))

def detail(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, 'carros/details.html', {'item':carro})



