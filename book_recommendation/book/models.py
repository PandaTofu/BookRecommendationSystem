from django.db import models
from book_type.models import BookType
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    # book
    name = models.CharField(max_length=60, verbose_name="book name", unique=True)
    author = models.CharField(max_length=30, verbose_name="author")
    cover = models.ImageField(verbose_name='cover', upload_to='book/image/%Y/%m', null=True, blank=True)
    pages = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="price")  # 书籍价格小数位为两位，整数位为3位
    desc = models.CharField(max_length=200, verbose_name="brief introduction")
    # information = HTMLField(max_length=200, verbose_name="information")
    genre = models.ForeignKey(
    	BookType, 
    	on_delete=models.CASCADE,
    	null=True, 
    	related_name='book',
    	verbose_name="genre")
    mark = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        default=0.0,
        verbose_name="mark",
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    N_mark = models.IntegerField(default=0)

    class Meta:
        verbose_name = "book"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('books:book_detail', arg=[self.id])

    def __str__(self):
        return self.name