# Generated by Django 3.2.24 on 2024-10-09 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_invest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invest',
            name='rate',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]
