# Generated by Django 4.1.3 on 2022-12-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_film_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='soup',
            field=models.CharField(default=None, max_length=200, verbose_name='РекСистем'),
        ),
    ]
