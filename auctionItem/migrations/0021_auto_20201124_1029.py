# Generated by Django 3.1.3 on 2020-11-24 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0020_auto_20201122_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='time_stamp',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 10, 29, 33, 22118)),
        ),
    ]
