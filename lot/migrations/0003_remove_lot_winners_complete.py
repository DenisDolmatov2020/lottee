# Generated by Django 3.1.2 on 2020-11-15 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lot', '0002_auto_20200920_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='winners_complete',
        ),
    ]
