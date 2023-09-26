from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255, default = '')
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default = '')
    amount = models.IntegerField(default = 0)
    artist = models.TextField(default = '')