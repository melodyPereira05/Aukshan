# Generated by Django 3.1.3 on 2020-11-27 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0024_auto_20201126_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lot_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 10, 40, 13, 133441)),
        ),
    ]
