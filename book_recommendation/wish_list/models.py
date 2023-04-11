from django.db import models
from user.models import User
from book.models import Book


# Create your models here.
class WishList(models.Model):
    title = models.CharField(max_length=60, verbose_name="title")
    desc = models.CharField(max_length=200, verbose_name="description")
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="wishlist", 
        verbose_name="user")

    class Meta:
        verbose_name = "wish list"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class BookWishListRelationship(models.Model):
    wish_list = models.ForeignKey(
        WishList, 
        on_delete=models.CASCADE,
        related_name="relationship", 
        verbose_name="user")
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE,
        related_name="relationship",  
        verbose_name="book")

    class Meta:
        verbose_name = "BW relationship"
        verbose_name_plural = verbose_name
        unique_together = ('wish_list', 'book')