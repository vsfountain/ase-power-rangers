from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    item_list = Item.objects.all()
    output = ''
    for i in item_list:
        output = output + i.item_name + ' ' + str(i.item_price) + '<br/>'
    return HttpResponse(output)
