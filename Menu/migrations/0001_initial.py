# Generated by Django 3.2.5 on 2022-02-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.IntegerField(default=1708, primary_key=True, serialize=False)),
                ('item_name', models.CharField(default='None', max_length=20)),
                ('item_desc', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='Main', max_length=10)),
                ('status', models.BooleanField(default='False')),
                ('price', models.FloatField(default=100.0)),
            ],
        ),
    ]