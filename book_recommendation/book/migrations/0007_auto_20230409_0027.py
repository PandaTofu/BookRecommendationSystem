# Generated by Django 3.2.18 on 2023-04-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20230408_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='desc'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=60, unique=True, verbose_name='name'),
        ),
    ]
