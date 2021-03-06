# Generated by Django 3.1.3 on 2020-11-27 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0026_auto_20201127_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 10, 46, 7, 804738)),
        ),
    ]
