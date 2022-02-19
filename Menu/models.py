from django.db import models
from random import randint

# Create your models here.
class Menu(models.Model):
    id = models.IntegerField(default=randint(1000, 9999), primary_key=True)
    item_name = models.CharField(max_length=20, default="None")
    item_desc = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=10, default="Main")
    status = models.BooleanField(default="False")
    price = models.FloatField(default=100.00)

    def __str__(self):
        return self.item_name
