# Generated by Django 3.2.18 on 2023-04-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preference_book', '0002_alter_preferencebook_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencebook',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
