# Generated by Django 5.1.3 on 2025-03-15 17:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BotModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('token', models.CharField(max_length=100, verbose_name='Token')),
            ],
            options={
                'verbose_name': 'BotModel',
                'verbose_name_plural': 'BotModels',
                'db_table': 'bot',
            },
        ),
        migrations.CreateModel(
            name='CarBrandModel',
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
                'verbose_name': 'CarbrandModel',
                'verbose_name_plural': 'CarbrandModels',
                'db_table': 'carbrand',
            },
        ),
        migrations.CreateModel(
            name='BotUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=1000, verbose_name='First name')),
                ('last_name', models.CharField(max_length=1000, verbose_name='Last name')),
                ('tg_id', models.IntegerField(verbose_name='Tg id')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.botmodel', verbose_name='bot')),
            ],
            options={
                'verbose_name': 'BotuserModel',
                'verbose_name_plural': 'BotuserModels',
                'db_table': 'botuser',
            },
        ),
        migrations.CreateModel(
            name='TaxiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('balance', models.BigIntegerField(verbose_name='balance')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'TaxiModel',
                'verbose_name_plural': 'TaxiModels',
                'db_table': 'taxi',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(verbose_name='number')),
                ('color', models.CharField(choices=[('red', 'red'), ('green', 'green'), ('black', 'black'), ('white', 'white')], verbose_name='color')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='api.carbrandmodel', verbose_name='car band')),
                ('taxi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='api.taximodel', verbose_name='taxi')),
            ],
            options={
                'verbose_name': 'CarModel',
                'verbose_name_plural': 'CarModels',
                'db_table': 'car',
            },
        ),
    ]
