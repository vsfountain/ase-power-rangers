from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from django.template import loader
from django.urls import reverse


def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('menu/index.html')
    context = {
        'item_list':item_list,
    }
    return HttpResponse(template.render(context, request))

