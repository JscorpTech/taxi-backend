# Generated by Django 5.1.3 on 2025-03-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_botmodel_tg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botmodel',
            name='tg_id',
            field=models.BigIntegerField(default=1, unique=True, verbose_name='tg_id'),
        ),
    ]
