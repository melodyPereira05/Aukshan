# Generated by Django 3.1.3 on 2020-11-14 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0010_auto_20201114_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 14, 23, 4, 13, 563157)),
        ),
    ]
