# Generated by Django 2.2.6 on 2019-11-01 11:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auction_base_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time_starting',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 1, 11, 2, 3, 574815, tzinfo=utc)),
            preserve_default=False,
        ),
    ]