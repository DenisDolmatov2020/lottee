# Generated by Django 3.1.1 on 2020-09-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
