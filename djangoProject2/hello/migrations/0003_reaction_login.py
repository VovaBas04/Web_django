# Generated by Django 4.1.3 on 2022-11-16 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_reaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='login',
            field=models.CharField(default=2, max_length=20, verbose_name='Логин'),
            preserve_default=False,
        ),
    ]
