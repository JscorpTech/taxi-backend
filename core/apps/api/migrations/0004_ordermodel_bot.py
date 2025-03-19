# Generated by Django 5.1.3 on 2025-03-19 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_locationmodel_botusermodel_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='bot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.botmodel', verbose_name='bot'),
        ),
    ]
