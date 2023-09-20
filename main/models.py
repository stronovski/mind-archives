from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, default = '')
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(default = 0)
    description = models.TextField(default = '')
    amount = models.IntegerField(default = 0)
    artist = models.TextField(default = '')