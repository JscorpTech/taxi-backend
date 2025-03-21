# Generated by Django 5.1.3 on 2025-03-19 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_ordermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'LocationModel',
                'verbose_name_plural': 'LocationModels',
                'db_table': 'location',
            },
        ),
        migrations.AddField(
            model_name='botusermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='location_lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Lat'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='location_long',
            field=models.FloatField(blank=True, null=True, verbose_name='Long'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='taxi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.taximodel', verbose_name='taxi'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='frm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frm_orders', to='api.locationmodel', verbose_name='from'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_orders', to='api.locationmodel', verbose_name='to'),
        ),
    ]
