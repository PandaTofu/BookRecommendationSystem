# Generated by Django 3.2.18 on 2023-04-09 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20230409_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='N_unuseful',
        ),
        migrations.RemoveField(
            model_name='book',
            name='N_useful',
        ),
    ]
