# Generated by Django 3.2.18 on 2023-04-10 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading_plan', '0003_auto_20230410_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingplan',
            name='last_clock_date',
            field=models.DateField(default=datetime.date(2023, 4, 9)),
        ),
    ]
