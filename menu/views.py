from django.http import HttpResponse

from django.core import serializers

import json

class Menu:
    def __init__(self,  products, phone):
        self.products = products
        self.phone = phone
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent =4)


    @staticmethod
    def create():
        product1 = Pizza('4 сыра', 100)
        product2 = Pizza('Маргарита', 120)
        menu = Menu([product1, product2], '+71111111')
        return menu

class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys=True, indent =4)


def index(request):
    x = 'Hello world 2.0!'
    menu = Menu.create()
    #data = serializers.serialize('json',menu.products[0])
    data = menu.toJSON()
    return HttpResponse(data, content_type='application/json')