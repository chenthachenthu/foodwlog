from django.contrib.auth.models import User
from django.db import models
from shop.models import *
# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=150,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=150)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField(null=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return str(self.prodt)