# Generated by Django 3.2.5 on 2022-02-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='person',
            new_name='persons',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.IntegerField(default=2273, primary_key=True, serialize=False),
        ),
    ]
