# Generated by Django 3.1.2 on 2020-11-22 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lot', '0005_remove_lot_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='lot/')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='lot.lot')),
            ],
        ),
        migrations.DeleteModel(
            name='LotImage',
        ),
    ]
