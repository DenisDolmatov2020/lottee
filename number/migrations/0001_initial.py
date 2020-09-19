# Generated by Django 3.1.1 on 2020-09-19 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lot', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(blank=True, default=1, verbose_name='Number')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date create')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date update')),
                ('won', models.BooleanField(default=False, verbose_name='winner')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lot', to='lot.lot')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
