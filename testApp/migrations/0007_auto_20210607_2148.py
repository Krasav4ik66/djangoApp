# Generated by Django 3.1.7 on 2021-06-07 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0006_auto_20210607_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 21, 48, 52, 542864)),
        ),
    ]
