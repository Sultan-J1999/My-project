# Generated by Django 4.2.5 on 2023-12-07 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]