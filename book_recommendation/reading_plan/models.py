from django.db import models

from user.models import User
from book.models import Book
from datetime import date, timedelta

# Create your models here.
class ReadingPlan(models.Model):
	book_name = models.CharField(max_length=60, verbose_name="book name", unique=True)
	period_days = models.IntegerField(verbose_name="reading period") #define how many days to finish the reading plan
	pages_per_day = models.IntegerField(verbose_name="pages per day")
	clock_days = models.IntegerField(default=0)
	last_clock_date = models.DateField(default=(date.today() + timedelta(days=-1)))
	is_completed = models.BooleanField(default=False)

	user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="plan", 
        verbose_name="user")

	class Meta:
		verbose_name = "reading plan"
		verbose_name_plural = verbose_name