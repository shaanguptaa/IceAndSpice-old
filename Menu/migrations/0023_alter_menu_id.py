# Generated by Django 3.2.5 on 2022-02-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0022_alter_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.IntegerField(default=9807, editable=False, primary_key=True, serialize=False),
        ),
    ]
