# Generated by Django 3.1.3 on 2020-11-27 05:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0025_auto_20201127_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 27, 10, 41, 32, 969615)),
        ),
    ]
