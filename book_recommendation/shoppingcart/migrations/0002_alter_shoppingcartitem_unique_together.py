# Generated by Django 3.2.18 on 2023-04-10 10:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20230409_2255'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shoppingcartitem',
            unique_together={('user', 'book')},
        ),
    ]