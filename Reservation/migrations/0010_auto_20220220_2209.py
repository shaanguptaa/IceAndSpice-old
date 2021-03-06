# Generated by Django 3.2.5 on 2022-02-20 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0009_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_booked',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 22, 9, 0, 792138)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_of_reservation',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 20, 22, 9, 0, 792138)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.IntegerField(default=6281, editable=False, primary_key=True, serialize=False),
        ),
    ]
