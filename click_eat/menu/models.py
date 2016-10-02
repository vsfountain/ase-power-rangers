from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dish(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
	submit_time = models.DateTimeField()
	payment = models.BooleanField()

class OrderDetail(models.Model):
	order = models.ForeignKey(Order)
	dish = models.ForeignKey(Dish)
	quantity = models.IntegerField()