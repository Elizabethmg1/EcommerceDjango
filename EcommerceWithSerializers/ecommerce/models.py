from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    client = models.CharField(max_length=30)

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order,related_name='products',on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)