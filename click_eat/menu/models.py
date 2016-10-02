from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=700)
    item_price = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return self.item_name
