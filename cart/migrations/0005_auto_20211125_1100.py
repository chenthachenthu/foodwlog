# Generated by Django 2.2 on 2021-11-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_items_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
