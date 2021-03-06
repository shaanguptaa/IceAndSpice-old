# Generated by Django 3.2.5 on 2022-02-21 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0020_auto_20220221_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_booked',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 21, 46, 5, 570864)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_of_reservation',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 21, 21, 46, 5, 570864)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.IntegerField(default=3973, editable=False, primary_key=True, serialize=False),
        ),
    ]
