# Generated by Django 4.1 on 2023-01-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reek', '0011_remove_category_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rating',
            field=models.FloatField(blank=True, default=0),
        ),
    ]