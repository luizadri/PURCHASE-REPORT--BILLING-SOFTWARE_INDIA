# Generated by Django 3.2.25 on 2024-03-28 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0005_alter_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 28)),
        ),
    ]
