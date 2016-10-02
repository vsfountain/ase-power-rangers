from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Menu(models.Model):
    name = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
    	return self.name

@python_2_unicode_compatible
class CustRecord(models.Model):
	name = models.CharField(max_length=20)
	time = models.DateTimeField()
	total_price = models.DecimalField(max_digits=6, decimal_places=2,default= 0)
	payment = models.BooleanField(default= False)
	def __str__(self):
		return self.name

class OrderRecord(models.Model):
	cust_id = models.ForeignKey(CustRecord, on_delete=models.CASCADE)
	dish_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
	served = models.BooleanField(default= False)