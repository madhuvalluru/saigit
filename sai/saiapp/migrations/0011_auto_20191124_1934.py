# Generated by Django 2.2 on 2019-11-24 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('saiapp', '0010_auto_20191124_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='register1',
            fields=[
                ('rgid', models.AutoField(primary_key=True, serialize=False)),
                ('rid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=250)),
                ('blood_group', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('creates', models.DateField(default=datetime.datetime(2019, 11, 24, 14, 4, 23, 762242, tzinfo=utc))),
                ('number', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]