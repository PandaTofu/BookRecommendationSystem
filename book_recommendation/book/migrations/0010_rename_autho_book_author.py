# Generated by Django 3.2.18 on 2023-04-09 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_book_autho'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='autho',
            new_name='author',
        ),
    ]