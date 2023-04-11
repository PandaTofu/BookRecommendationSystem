from django.db import models

from user.models import User
from book.models import Book

# Create your models here.
class PreferenceBook(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="reviews", 
        verbose_name="user")
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE,
        related_name="reviews",  
        verbose_name="book")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "preference book"
        verbose_name_plural = verbose_name
        unique_together = ('user', 'book')