from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from .models import Menu, CustRecord, OrderRecord
from django.utils import timezone
#from django.urls import reverse
from django.core.urlresolvers import reverse

def index(request):
	list_of_pie = Menu.objects.all()
	#template = loader.get_template('choose/index.html')
	context = {
	    'list_of_pie': list_of_pie,
	}
	return render(request, 'choose/index.html', context)
	#return HttpResponse(template.render(context, request))
	#return HttpResponse(template.render(context, request))

def submit(request):
	cust = CustRecord(name=request.POST["name"], time=timezone.now())
	price = 0
	cust.save()
	menu = Menu.objects.all()
	for dish in menu:
		try:
			tmp = request.POST['dish' + str(dish.id)]
		#if tmp == "1":
			price += dish.cost
			cust.orderrecord_set.create(dish_id = dish)
		except:
			continue
	cust.total_price = price
	cust.save()
	return HttpResponseRedirect(reverse('result', args=(cust.id,)))

def result(request, cust_id):
    cust = get_object_or_404(CustRecord, pk=cust_id)
    cust_order = cust.orderrecord_set.all()
    menu_array = []
    for i in cust_order:
    	menu_array.append(i.dish_id)
    return render(request, 'choose/result.html', {'cust': cust, 'menu':menu_array})