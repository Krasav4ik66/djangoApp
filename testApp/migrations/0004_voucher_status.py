# Generated by Django 3.1.7 on 2021-06-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_remove_voucher_destinationcity'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='status',
            field=models.CharField(default='In progress', max_length=20),
            preserve_default=False,
        ),
    ]