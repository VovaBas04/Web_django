# Generated by Django 4.1.3 on 2022-12-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_remove_film_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='recsys',
            field=models.BooleanField(default=None, verbose_name='Система рекомендаций'),
        ),
    ]