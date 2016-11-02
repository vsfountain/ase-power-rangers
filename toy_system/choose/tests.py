from django.test import TestCase
from choose.models import *
# Create your tests here.
from django.core.urlresolvers import reverse
def create_dish(name, cost):
	return Menu.objects.create(name = name, cost = cost)

class MenuViewTests(TestCase):
	def test_index_view_with_one_dish(self):
		create_dish(name = "apple pie", cost = 1.32)
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(
			response.context['list_of_pie'],
			['<Menu: apple pie>']
		)

	def test_index_view_with_zero_dish(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code,200)
		self.assertQuerysetEqual(
			response.context['list_of_pie'],
			[]
		)