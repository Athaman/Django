from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=400)
    price = models.FloatField()
    description = models.TextField()
    imglink = models.CharField(max_length = 400)

class Order(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    payment_method = models.CharField(max_length = 100)
    payment_data = models.CharField(max_length = 50)
    items = models.TextField()
    fulfilled = models.BooleanField()
