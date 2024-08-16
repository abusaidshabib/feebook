from django.db import models
from authentication.models import BaseModel, CustomUser
from Contents.models import Photo

TYPES = [('online','Online'),('offline','Offline')]
PAYMENT_METHOD = [('bkash','Bkash'),('rocket','Rocket'),('cash_on_delivery','Cash On Delivery')]

class Category(BaseModel):
    name = models.CharField(max_length=100)

class SubCategory(BaseModel):
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Products(BaseModel):
    subcategory = models.ForeignKey(SubCategory,related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    photo = models.ForeignKey(Photo, related_name='product', on_delete=models.CASCADE)
    saler = models.ForeignKey(CustomUser, related_name="product", on_delete=models.CASCADE)

class Order(BaseModel):
    buyer = models.ForeignKey(CustomUser, related_name="order", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="order", on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TYPES)
    quantity = models.IntegerField()
    total_price = models.FloatField()


class Payment(BaseModel):
    order = models.ForeignKey(Order, related_name="payment", on_delete=models.CASCADE)
    method = models.CharField(max_length=100, choices=PAYMENT_METHOD)
    due = models.FloatField(default=0.0)
    delivery_status = models.BooleanField()