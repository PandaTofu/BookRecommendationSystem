from django.db import models
from datetime import datetime

from user.models import User
from book.models import Book

# Create your models here.
class BookReview(models.Model):
    # book review
    text = models.TextField()
    date_publish = models.DateTimeField(
        verbose_name="published date", 
        auto_now=True)
    # review = HTMLField(max_length=200, verbose_name="用户评论")
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="review", 
        verbose_name="user")
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE,
        related_name="review",  
        verbose_name="book")
    N_useful = models.IntegerField(default=0)
    N_not_useful = models.IntegerField(default=0)

    class Meta:
        verbose_name = "book review"
        verbose_name_plural = verbose_name
        ordering = ('-date_publish', )

    def __str__(self):
        return self.text[:20]