# Generated by Django 3.1.2 on 2020-12-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_user', '0003_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=32, null=True, unique=True, verbose_name='phone_number'),
        ),
    ]
