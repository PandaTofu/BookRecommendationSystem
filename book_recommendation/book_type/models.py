from django.db import models

# Create your models here.
class BookType(models.Model):
    # book type
    book_type = models.CharField(max_length=20, verbose_name="type")

    class Meta:
        verbose_name = "book type"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_type