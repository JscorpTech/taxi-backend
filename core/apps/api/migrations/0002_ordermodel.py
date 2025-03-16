# Generated by Django 5.1.3 on 2025-03-15 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('frm', models.TextField(verbose_name='from')),
                ('to', models.TextField(verbose_name='to')),
                ('price', models.PositiveBigIntegerField(verbose_name='price')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='count')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.botusermodel', verbose_name='user')),
            ],
            options={
                'verbose_name': 'OrderModel',
                'verbose_name_plural': 'OrderModels',
                'db_table': 'order',
            },
        ),
    ]
