# Generated by Django 3.2.5 on 2022-02-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0005_auto_20220220_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.IntegerField(default=4574, editable=False, primary_key=True, serialize=False),
        ),
    ]