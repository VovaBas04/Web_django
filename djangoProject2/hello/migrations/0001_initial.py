# Generated by Django 4.1.3 on 2022-11-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
            ],
        ),
    ]
