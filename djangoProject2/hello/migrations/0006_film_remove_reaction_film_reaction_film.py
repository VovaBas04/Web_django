# Generated by Django 4.1.3 on 2022-11-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_reaction_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название фильма')),
            ],
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='Film',
        ),
        migrations.AddField(
            model_name='reaction',
            name='film',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='hello.film'),
            preserve_default=False,
        ),
    ]