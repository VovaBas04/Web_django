# Generated by Django 4.1.3 on 2022-11-17 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_reaction_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.autorization'),
        ),
    ]
