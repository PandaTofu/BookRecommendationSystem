from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = (
        (0, 'unknown'),
        (1, 'man'),
        (2, 'female')
    )
    email = models.EmailField(max_length=255, verbose_name="email", null=True, blank=True, help_text="email")
    avatar = models.CharField(max_length=255, verbose_name="avatar", null=True, blank=True, help_text="avatar")
    # avatar = models.FileField(verbose_name="avatar", upload_to='avatar', default='avatar/default.jpg')
    gender = models.IntegerField(
        choices=GENDER_CHOICES, default=0, verbose_name="gender", null=True, blank=True, help_text="gender"
    )

    class Meta:
        db_table = "system_users"
        verbose_name = "User"
        verbose_name_plural = verbose_name
        ordering = ("date_joined",)
