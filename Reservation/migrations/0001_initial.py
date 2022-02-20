# Generated by Django 3.2.5 on 2022-02-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.IntegerField(default=5173, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('person', models.IntegerField(default=1)),
            ],
        ),
    ]