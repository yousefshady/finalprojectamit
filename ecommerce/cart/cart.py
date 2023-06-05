from django.conf import settings
from main.models import Product
from django.db import models

class Cart(models.Model):
    def __init__(self, req):
        self.session = req.session
        cart=self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart=self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(id=p)

        for item in self.cart.values():
            item['total_price'] = int(item['product'].price * item['quantity'])
            yield item
    
    def __len__(self):
        if sum(item['quantity'] for item in self.cart.values()) >= 0:
            return sum(item['quantity'] for item in self.cart.values())
        else: return 0
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified=True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id=product_id
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id':product_id}
            
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def gettotalcost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(id=p)
        cost=int(sum((item['product'].price - item['product'].sale_price) * item['quantity'] for item in self.cart.values()))
        if cost >= 0:
            return cost
        else:
            return 0
    def getquantity(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(id=p)
        if int(sum(item['quantity'] for item in self.cart.values())) >=0:
            return int(sum(item['quantity'] for item in self.cart.values()))
        else:
            return 0