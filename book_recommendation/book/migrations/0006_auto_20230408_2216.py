# Generated by Django 3.2.18 on 2023-04-08 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_type', '0001_initial'),
        ('book', '0005_alter_book_b_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='brief_introduction',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='b_type',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_pic',
        ),
        migrations.AddField(
            model_name='book',
            name='N_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='N_unuseful',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='N_useful',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book/image/%Y/%m', verbose_name='cover'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='book_type.booktype', verbose_name='genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='mark',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3, verbose_name='mark'),
        ),
    ]
