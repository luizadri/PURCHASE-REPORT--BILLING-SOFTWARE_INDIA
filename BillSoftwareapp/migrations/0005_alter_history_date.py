# Generated by Django 3.2.25 on 2024-03-27 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSoftwareapp', '0004_auto_20240325_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 27)),
        ),
    ]
