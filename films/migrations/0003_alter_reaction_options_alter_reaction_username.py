# Generated by Django 4.1.3 on 2022-11-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_film_options_reaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reaction',
            options={'verbose_name': 'Реакция пользователя', 'verbose_name_plural': 'Реакции Пользователей'},
        ),
        migrations.AlterField(
            model_name='reaction',
            name='username',
            field=models.CharField(max_length=20, verbose_name='Имя пользователя'),
        ),
    ]
