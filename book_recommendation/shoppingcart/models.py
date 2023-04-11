from django.db import models

from book.models import Book
from user.models import User


# Create your models here.
class ShoppingCartItem(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="shoppingcart", 
        verbose_name="user")
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE,
        related_name="shoppingcart",  
        verbose_name="book")

    class Meta:
        verbose_name = "shopping cart item"
        verbose_name_plural = verbose_name
        unique_together = ('user', 'book')