# Generated by Django 4.1.3 on 2022-12-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_alter_reaction_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='overflew',
            field=models.CharField(default=None, max_length=300, verbose_name='Описание'),
        ),
    ]
