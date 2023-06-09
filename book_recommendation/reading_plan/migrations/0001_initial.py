# Generated by Django 3.2.18 on 2023-04-04 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0005_alter_book_b_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField(verbose_name='reading period')),
                ('pages_per_day', models.IntegerField(verbose_name='pages_per_day')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='book.book', verbose_name='book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'reading plan',
                'verbose_name_plural': 'reading plan',
            },
        ),
    ]
