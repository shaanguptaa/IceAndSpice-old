# Generated by Django 3.2.5 on 2022-02-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0015_alter_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.CharField(default='M5105', editable=False, max_length=5, primary_key=True, serialize=False),
        ),
    ]