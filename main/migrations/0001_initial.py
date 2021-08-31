# Generated by Django 3.2.6 on 2021-08-31 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('Email', models.CharField(max_length=50, verbose_name='Email')),
                ('school', models.CharField(max_length=50, verbose_name='Название школы и №')),
                ('age', models.CharField(max_length=50, verbose_name='Возраст')),
                ('grade', models.CharField(max_length=50, verbose_name='Класс')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО родителя')),
                ('number_fio', models.CharField(max_length=50, verbose_name='Телефон родителя')),
            ],
        ),
    ]
