# Generated by Django 3.0.7 on 2020-06-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pickup', '0004_auto_20200605_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickup',
            name='odoMeter',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
