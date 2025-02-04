# Generated by Django 4.2.13 on 2024-07-02 15:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категорія')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HolidayHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Будинок відпочинку')),
            ],
            options={
                'verbose_name': 'Будинок відпочинку',
                'verbose_name_plural': 'Будинок відпочинку',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PostClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Текст')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Зображення')),
                ('document', models.FileField(blank=True, upload_to='documents/%Y/%m/%d/', verbose_name='Додаток')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Змінено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публікація')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.categoryclass', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Допис головного додатку',
                'verbose_name_plural': 'Дописи головного додатку',
                'ordering': ['-time_create', 'title'],
            },
        ),
        migrations.CreateModel(
            name='BookingHouseClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('booking_pets', models.TextField(blank=True, max_length=255, verbose_name='Домашні улюбленці')),
                ('booking_wish', models.TextField(blank=True, max_length=255, verbose_name='Додаткові послуги')),
                ('time', models.CharField(choices=[('15:00', '15:00')], default='15:00', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('holidayhouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.holidayhouse', verbose_name='Будинок відпочинку')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Бронювання будинку відпочинку',
                'verbose_name_plural': 'Бронювання будинків відпочинку',
                'ordering': ['id'],
            },
        ),
    ]
