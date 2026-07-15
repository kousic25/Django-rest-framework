from django.db import models
from django.contrib.auth.models import User
from menucard.models import Food   


class CartItem(models.Model):
    username = models.CharField(max_length=150)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.username} - {self.food.name}"